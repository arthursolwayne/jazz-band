
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=1.5),     # Hihat on every 8th
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)   # Kick on 3
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Marcus - walking line in Dm, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=1.875),   # D2 (root)
    pretty_midi.Note(velocity=90, pitch=53, start=1.875, end=2.25),  # F2 (fifth)
    pretty_midi.Note(velocity=90, pitch=51, start=2.25, end=2.625),  # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=50, start=2.625, end=3.0),   # D2 (root)

    pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=3.375),   # D2
    pretty_midi.Note(velocity=90, pitch=53, start=3.375, end=3.75),  # F2
    pretty_midi.Note(velocity=90, pitch=51, start=3.75, end=4.125),  # Eb2
    pretty_midi.Note(velocity=90, pitch=50, start=4.125, end=4.5),   # D2

    pretty_midi.Note(velocity=90, pitch=50, start=4.5, end=4.875),   # D2
    pretty_midi.Note(velocity=90, pitch=53, start=4.875, end=5.25),  # F2
    pretty_midi.Note(velocity=90, pitch=51, start=5.25, end=5.625),  # Eb2
    pretty_midi.Note(velocity=90, pitch=50, start=5.625, end=6.0)    # D2
]
bass.notes.extend(bass_notes)

# Piano: Diane - open voicings, different chords each bar, resolve on the last
# Bar 2: Dm7 (D F A C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # C5

    # Bar 3: Gm7 (G Bb D F)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # Bb4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # D5
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.375),  # F5

    # Bar 4: Cm7 (C Eb G Bb)
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875),  # C5
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.875),  # Eb5
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.875),  # G5
    pretty_midi.Note(velocity=100, pitch=77, start=4.5, end=4.875),  # Bb5
]
piano.notes.extend(piano_notes)

# Drums: Bar 2-4
for bar_start in [1.5, 3.0, 4.5]:
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.75, end=bar_start + 1.125)
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.875, end=bar_start + 2.25)
    # Hihat on every eighth
    for i in range(4):
        pretty_midi.Note(velocity=90, pitch=42, start=bar_start + i * 0.375, end=bar_start + i * 0.375 + 0.375)

# Sax: Dante - One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.625), # A4
    pretty_midi.Note(velocity=110, pitch=65, start=3.375, end=3.75), # F4
    pretty_midi.Note(velocity=110, pitch=67, start=4.125, end=4.5),  # A4
    pretty_midi.Note(velocity=110, pitch=65, start=4.875, end=5.25), # F4
    pretty_midi.Note(velocity=110, pitch=67, start=5.625, end=6.0)   # A4
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
