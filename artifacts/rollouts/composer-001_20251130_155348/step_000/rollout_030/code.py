
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.125),
    pretty_midi.Note(velocity=100, pitch=42, start=0.125, end=0.25),
    pretty_midi.Note(velocity=100, pitch=42, start=0.25, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.5),
    pretty_midi.Note(velocity=100, pitch=42, start=0.5, end=0.625),
    pretty_midi.Note(velocity=100, pitch=42, start=0.625, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=42, start=0.875, end=1.0),
    pretty_midi.Note(velocity=100, pitch=42, start=1.0, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.25),
    pretty_midi.Note(velocity=100, pitch=42, start=1.25, end=1.375),
    pretty_midi.Note(velocity=100, pitch=42, start=1.375, end=1.5),
]

drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: walking line, chromatic approaches, never the same note twice
# F7 - F7 - F7 - F7
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=47, start=1.5, end=1.625), # F
    pretty_midi.Note(velocity=100, pitch=48, start=1.625, end=1.75), # G
    pretty_midi.Note(velocity=100, pitch=50, start=1.75, end=1.875), # A
    pretty_midi.Note(velocity=100, pitch=49, start=1.875, end=2.0), # Ab
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=50, start=2.0, end=2.125), # A
    pretty_midi.Note(velocity=100, pitch=48, start=2.125, end=2.25), # G
    pretty_midi.Note(velocity=100, pitch=47, start=2.25, end=2.375), # F
    pretty_midi.Note(velocity=100, pitch=49, start=2.375, end=2.5), # Ab
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=49, start=2.5, end=2.625), # Ab
    pretty_midi.Note(velocity=100, pitch=47, start=2.625, end=2.75), # F
    pretty_midi.Note(velocity=100, pitch=48, start=2.75, end=2.875), # G
    pretty_midi.Note(velocity=100, pitch=50, start=2.875, end=3.0), # A
]
bass.notes.extend(bass_notes)

# Diane on piano: 7th chords, comp on 2 and 4
# F7 (F A C Eb)
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.75), # F
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.75), # A
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=1.75), # C
    pretty_midi.Note(velocity=100, pitch=75, start=1.5, end=1.75), # Eb
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.5), # F
    pretty_midi.Note(velocity=100, pitch=76, start=2.25, end=2.5), # A
    pretty_midi.Note(velocity=100, pitch=79, start=2.25, end=2.5), # C
    pretty_midi.Note(velocity=100, pitch=75, start=2.25, end=2.5), # Eb
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=72, start=2.5, end=2.75), # F
    pretty_midi.Note(velocity=100, pitch=76, start=2.5, end=2.75), # A
    pretty_midi.Note(velocity=100, pitch=79, start=2.5, end=2.75), # C
    pretty_midi.Note(velocity=100, pitch=75, start=2.5, end=2.75), # Eb
]
piano.notes.extend(piano_notes)

# You on sax: one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# F - Bb - D - F (intervallic motif, not a scale run)
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.625), # F
    pretty_midi.Note(velocity=110, pitch=60, start=1.625, end=1.75), # Bb
    pretty_midi.Note(velocity=110, pitch=63, start=1.75, end=1.875), # D
    pretty_midi.Note(velocity=110, pitch=66, start=1.875, end=2.0), # F
    # Bar 3
    pretty_midi.Note(velocity=110, pitch=66, start=2.0, end=2.125), # F
    pretty_midi.Note(velocity=110, pitch=60, start=2.125, end=2.25), # Bb
    pretty_midi.Note(velocity=110, pitch=63, start=2.25, end=2.375), # D
    # Bar 4
    pretty_midi.Note(velocity=110, pitch=66, start=2.875, end=3.0), # F
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    # Kick
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5),
    # Snare
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.875, end=start + 2.0),
    # Hi-hat
    for i in range(0, 4):
        pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125),

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_russo_intro.mid")
