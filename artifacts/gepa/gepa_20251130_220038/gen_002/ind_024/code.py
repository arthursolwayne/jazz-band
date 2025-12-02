
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
    
    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=100, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=100, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: walking line in Fm, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2: Fm (F, Ab, D, C) - walking line starting on F
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=1.625, end=1.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=70, start=1.75, end=1.875),  # E
    pretty_midi.Note(velocity=100, pitch=68, start=1.875, end=2.0),  # D

    # Bar 3: Fm (F, Ab, D, C)
    pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.125),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=2.125, end=2.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.375),  # D#
    pretty_midi.Note(velocity=100, pitch=68, start=2.375, end=2.5),  # D

    # Bar 4: Fm (F, Ab, D, C)
    pretty_midi.Note(velocity=100, pitch=71, start=2.5, end=2.625),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=2.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=68, start=2.75, end=2.875),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=2.875, end=3.0),  # C#
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: F7 on 2 and 4 (Ab, C, F, E)
    pretty_midi.Note(velocity=100, pitch=70, start=1.75, end=1.875),  # E
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=1.875),  # Eb
    pretty_midi.Note(velocity=100, pitch=71, start=1.75, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=1.75, end=1.875),  # D

    pretty_midi.Note(velocity=100, pitch=70, start=1.875, end=2.0),  # E
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=1.875, end=2.0),  # D

    # Bar 3: F7 on 2 and 4 (Ab, C, F, E)
    pretty_midi.Note(velocity=100, pitch=70, start=2.25, end=2.375),  # E
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.375),  # Eb
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.375),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=2.25, end=2.375),  # D

    pretty_midi.Note(velocity=100, pitch=70, start=2.375, end=2.5),  # E
    pretty_midi.Note(velocity=100, pitch=69, start=2.375, end=2.5),  # Eb
    pretty_midi.Note(velocity=100, pitch=71, start=2.375, end=2.5),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=2.375, end=2.5),  # D

    # Bar 4: F7 on 2 and 4 (Ab, C, F, E)
    pretty_midi.Note(velocity=100, pitch=70, start=2.75, end=2.875),  # E
    pretty_midi.Note(velocity=100, pitch=69, start=2.75, end=2.875),  # Eb
    pretty_midi.Note(velocity=100, pitch=71, start=2.75, end=2.875),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=2.75, end=2.875),  # D

    pretty_midi.Note(velocity=100, pitch=70, start=2.875, end=3.0),  # E
    pretty_midi.Note(velocity=100, pitch=69, start=2.875, end=3.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=71, start=2.875, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=2.875, end=3.0),  # D
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it. No scale runs.
# Fm motif: F, Ab, D, C
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=110, pitch=69, start=1.625, end=1.75),  # Eb
    pretty_midi.Note(velocity=110, pitch=70, start=1.75, end=1.875),  # E
    pretty_midi.Note(velocity=110, pitch=68, start=1.875, end=2.0),  # D

    pretty_midi.Note(velocity=110, pitch=69, start=2.5, end=2.625),  # Eb
    pretty_midi.Note(velocity=110, pitch=71, start=2.625, end=2.75),  # F
    pretty_midi.Note(velocity=110, pitch=68, start=2.75, end=2.875),  # D
    pretty_midi.Note(velocity=110, pitch=67, start=2.875, end=3.0),  # C#
]
sax.notes.extend(sax_notes)

# Drums: Bars 2-4
# Kick on 1 and 3
for bar in range(2, 5):
    start = bar * 1.5
    kick_start = start
    kick_end = start + 0.375
    kick_3_start = start + 1.125
    kick_3_end = start + 1.5
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_end))
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick_3_start, end=kick_3_end))

# Snare on 2 and 4
for bar in range(2, 5):
    start = bar * 1.5
    snare_2_start = start + 0.75
    snare_2_end = start + 0.875
    snare_4_start = start + 1.875
    snare_4_end = start + 2.0
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=snare_2_start, end=snare_2_end))
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=snare_4_start, end=snare_4_end))

# Hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    for i in range(8):
        hihat_start = start + i * 0.1875
        hihat_end = hihat_start + 0.1875
        drum_notes.append(pretty_midi.Note(velocity=100, pitch=42, start=hihat_start, end=hihat_end))

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_russo_intro.mid")
