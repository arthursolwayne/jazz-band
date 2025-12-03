
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    # Kick on beat 1
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    # Hi-hat on beat 1 & 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    # Snare on beat 2
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=1.125),
    # Hi-hat on beat 3 & 4
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    # Kick on beat 3
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on beat 4
    pretty_midi.Note(velocity=110, pitch=38, start=1.5, end=1.875),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line in Dm, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=1.875),   # D2
    pretty_midi.Note(velocity=90, pitch=53, start=1.875, end=2.25),  # F2
    pretty_midi.Note(velocity=90, pitch=51, start=2.25, end=2.625),  # Eb2 (chromatic approach to F)
    pretty_midi.Note(velocity=90, pitch=55, start=2.625, end=3.0),   # A2

    # Bar 3
    pretty_midi.Note(velocity=90, pitch=55, start=3.0, end=3.375),   # A2
    pretty_midi.Note(velocity=90, pitch=50, start=3.375, end=3.75),  # D2
    pretty_midi.Note(velocity=90, pitch=49, start=3.75, end=4.125),  # C2 (chromatic approach to D)
    pretty_midi.Note(velocity=90, pitch=53, start=4.125, end=4.5),   # F2

    # Bar 4
    pretty_midi.Note(velocity=90, pitch=53, start=4.5, end=4.875),   # F2
    pretty_midi.Note(velocity=90, pitch=55, start=4.875, end=5.25),  # A2
    pretty_midi.Note(velocity=90, pitch=56, start=5.25, end=5.625),  # Bb2 (chromatic approach to A)
    pretty_midi.Note(velocity=90, pitch=50, start=5.625, end=6.0),   # D2
]
bass.notes.extend(bass_notes)

# Piano (Diane): Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D F Ab C)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875), # D4
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.875), # F4
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.875), # Ab4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875), # C5

    # Bar 3: G7 (G B D F)
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375), # G4
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375), # B4
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375), # D5
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.375), # F5

    # Bar 4: Cm7 (C Eb G Bb)
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.875), # C4
    pretty_midi.Note(velocity=90, pitch=63, start=4.5, end=4.875), # Eb4
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875), # G4
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875), # Bb4
]
piano.notes.extend(piano_notes)

# Saxophone (Dante): One short motif, haunting and incomplete
sax_notes = [
    # Bar 2: Start the motif
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75), # F4
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),  # G4
    pretty_midi.Note(velocity=100, pitch=64, start=2.0, end=2.25),  # E4

    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # D4
    pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.5),  # E4
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.75),  # D4

    # Bar 4: Come back and finish it
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.75),  # G4
    pretty_midi.Note(velocity=100, pitch=65, start=4.75, end=5.0),  # F4
    pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.25),  # D4
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4: Kick on 1 & 3, snare on 2 & 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    # Hi-hat on 1 & 2
    pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 1.125)
    # Snare on 2
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 1.125)
    # Hi-hat on 3 & 4
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.5)
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.5, end=start + 1.875)
    # Kick on 3
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare on 4
    pretty_midi.Note(velocity=110, pitch=38, start=start + 1.5, end=start + 1.875)
    drums.notes.extend([

        pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375),
        pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.375),
        pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 1.125),
        pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 1.125),
        pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.5),
        pretty_midi.Note(velocity=80, pitch=42, start=start + 1.5, end=start + 1.875),
        pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5),
        pretty_midi.Note(velocity=110, pitch=38, start=start + 1.5, end=start + 1.875),
    ])

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
