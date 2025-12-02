
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=61, start=1.875, end=2.25), # C
    pretty_midi.Note(velocity=90, pitch=63, start=2.25, end=2.625), # Eb
    pretty_midi.Note(velocity=90, pitch=64, start=2.625, end=3.0),  # F
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=90, pitch=66, start=3.375, end=3.75), # Ab
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.125), # F
    pretty_midi.Note(velocity=90, pitch=62, start=4.125, end=4.5),  # D
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=63, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=90, pitch=61, start=4.875, end=5.25), # C
    pretty_midi.Note(velocity=90, pitch=65, start=5.25, end=5.625), # G
    pretty_midi.Note(velocity=90, pitch=64, start=5.625, end=6.0),  # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Dm7 on 2 and 4
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.25), # D
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25), # F
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25), # A
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.25), # C
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75), # D
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75), # F
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75), # A
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75), # C
    # Bar 3: Dm7 on 2 and 4
    pretty_midi.Note(velocity=100, pitch=62, start=3.875, end=4.25), # D
    pretty_midi.Note(velocity=100, pitch=67, start=3.875, end=4.25), # F
    pretty_midi.Note(velocity=100, pitch=69, start=3.875, end=4.25), # A
    pretty_midi.Note(velocity=100, pitch=71, start=3.875, end=4.25), # C
    pretty_midi.Note(velocity=100, pitch=62, start=5.375, end=5.75), # D
    pretty_midi.Note(velocity=100, pitch=67, start=5.375, end=5.75), # F
    pretty_midi.Note(velocity=100, pitch=69, start=5.375, end=5.75), # A
    pretty_midi.Note(velocity=100, pitch=71, start=5.375, end=5.75), # C
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D - F - Bb - D
# Bar 2: D (62), F (67), Bb (67-1), D (62) -> D - F - Bb - D
# Bar 3: D - F - Bb - D
# Bar 4: D - F - Bb - D

sax_notes = [
    # Bar 2: D - F - Bb - D
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=110, pitch=67, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=110, pitch=64, start=1.875, end=2.125),
    pretty_midi.Note(velocity=110, pitch=62, start=2.125, end=2.25),
    # Bar 3: D - F - Bb - D
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=110, pitch=67, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=110, pitch=64, start=3.375, end=3.625),
    pretty_midi.Note(velocity=110, pitch=62, start=3.625, end=3.75),
    # Bar 4: D - F - Bb - D
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=110, pitch=67, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=110, pitch=64, start=4.875, end=5.125),
    pretty_midi.Note(velocity=110, pitch=62, start=5.125, end=5.25),
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar_start = 1.5
for bar in range(2, 5):
    # Kick on 1 and 3
    kick_start = bar_start + 0.0
    kick_end = kick_start + 0.375
    pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_end)
    kick_start = bar_start + 1.125
    kick_end = kick_start + 0.375
    pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_end)
    # Snare on 2 and 4
    snare_start = bar_start + 0.75
    snare_end = snare_start + 0.125
    pretty_midi.Note(velocity=110, pitch=38, start=snare_start, end=snare_end)
    snare_start = bar_start + 1.875
    snare_end = snare_start + 0.125
    pretty_midi.Note(velocity=110, pitch=38, start=snare_start, end=snare_end)
    # Hihat on every eighth
    for i in range(8):
        hihat_start = bar_start + i * 0.375
        hihat_end = hihat_start + 0.1875
        pretty_midi.Note(velocity=90, pitch=42, start=hihat_start, end=hihat_end)
    bar_start += 1.5

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
