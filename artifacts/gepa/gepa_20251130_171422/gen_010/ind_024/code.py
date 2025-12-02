
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass - Marcus: Walking line, chromatic approaches, never the same note twice
# F7 chord: F, A, C, E
# Walking line in F minor (F, Gb, G, Ab, A, Bb, B, C)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=70, start=1.5, end=1.875),   # F (7th fret E string)
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.25),  # Gb (6th fret E string)
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.625),  # G (7th fret D string)
    pretty_midi.Note(velocity=90, pitch=70, start=2.625, end=3.0),   # F
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.375),   # A
    pretty_midi.Note(velocity=90, pitch=71, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.125),  # Gb
    pretty_midi.Note(velocity=90, pitch=70, start=4.125, end=4.5),   # F
    pretty_midi.Note(velocity=90, pitch=74, start=4.5, end=4.875),   # C
    pretty_midi.Note(velocity=90, pitch=72, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=90, pitch=73, start=5.25, end=5.625),  # Bb
    pretty_midi.Note(velocity=90, pitch=74, start=5.625, end=6.0),   # C
]
bass.notes.extend(bass_notes)

# Diane on piano: 7th chords, comp on 2 and 4
# F7 = F, A, C, E
# F7 on 2 and 4
piano_notes = [
    # Bar 2 - F7 on 2
    pretty_midi.Note(velocity=95, pitch=70, start=2.25, end=2.625),   # F (7th fret E string)
    pretty_midi.Note(velocity=95, pitch=72, start=2.25, end=2.625),   # A
    pretty_midi.Note(velocity=95, pitch=74, start=2.25, end=2.625),   # C
    pretty_midi.Note(velocity=95, pitch=76, start=2.25, end=2.625),   # E
    # Bar 3 - F7 on 2
    pretty_midi.Note(velocity=95, pitch=70, start=3.75, end=4.125),   # F
    pretty_midi.Note(velocity=95, pitch=72, start=3.75, end=4.125),   # A
    pretty_midi.Note(velocity=95, pitch=74, start=3.75, end=4.125),   # C
    pretty_midi.Note(velocity=95, pitch=76, start=3.75, end=4.125),   # E
    # Bar 4 - F7 on 2
    pretty_midi.Note(velocity=95, pitch=70, start=5.25, end=5.625),   # F
    pretty_midi.Note(velocity=95, pitch=72, start=5.25, end=5.625),   # A
    pretty_midi.Note(velocity=95, pitch=74, start=5.25, end=5.625),   # C
    pretty_midi.Note(velocity=95, pitch=76, start=5.25, end=5.625),   # E
]
piano.notes.extend(piano_notes)

# Dante on sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F, Gb, F, Eb
# F (66), Gb (67), F (66), Eb (64)
# Bar 2: Start motif
# Bar 3: Leave it hanging (rest)
# Bar 4: Finish it

sax_notes = [
    pretty_midi.Note(velocity=110, pitch=66, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.625),  # Gb
    pretty_midi.Note(velocity=110, pitch=66, start=2.625, end=3.0),   # F
    pretty_midi.Note(velocity=110, pitch=64, start=3.0, end=3.375),   # Eb
    # Bar 3: rest
    # Bar 4: repeat motif
    pretty_midi.Note(velocity=110, pitch=66, start=4.5, end=4.875),   # F
    pretty_midi.Note(velocity=110, pitch=67, start=4.875, end=5.25),  # Gb
    pretty_midi.Note(velocity=110, pitch=66, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=110, pitch=64, start=5.625, end=6.0),   # Eb
]
sax.notes.extend(sax_notes)

# Drums: Bars 2-4
# Kick on 1 and 3
# Snare on 2 and 4
# Hihat on every eighth
for bar in range(2, 4):
    bar_start = 1.5 + bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 0.0, end=bar_start + 0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=bar_start + 0.75, end=bar_start + 0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=bar_start + 1.875, end=bar_start + 2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 0.0, end=bar_start + 0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 0.1875, end=bar_start + 0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 0.375, end=bar_start + 0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 0.5625, end=bar_start + 0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 0.75, end=bar_start + 0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 0.9375, end=bar_start + 1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 1.125, end=bar_start + 1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 1.3125, end=bar_start + 1.5),

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_russo_intro.mid")
