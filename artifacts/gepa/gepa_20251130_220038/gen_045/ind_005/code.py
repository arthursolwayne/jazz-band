
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes_bar1 = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.75),  # Hihat on 1 & 2
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5), # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.5),  # Hihat on 3 & 4
]
drums.notes.extend(drum_notes_bar1)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus) - Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=45, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=46, start=1.875, end=2.25), # F#
    pretty_midi.Note(velocity=90, pitch=47, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=90, pitch=49, start=2.625, end=3.0),  # A
    pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=3.375),  # A#
    pretty_midi.Note(velocity=90, pitch=51, start=3.375, end=3.75), # B
    pretty_midi.Note(velocity=90, pitch=53, start=3.75, end=4.125), # C
    pretty_midi.Note(velocity=90, pitch=54, start=4.125, end=4.5),  # C#
    pretty_midi.Note(velocity=90, pitch=55, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=90, pitch=57, start=4.875, end=5.25), # E
    pretty_midi.Note(velocity=90, pitch=58, start=5.25, end=5.625), # F
    pretty_midi.Note(velocity=90, pitch=59, start=5.625, end=6.0),  # F#
]
bass.notes.extend(bass_notes)

# Piano (Diane) - 7th chords on 2 and 4
piano_notes = [
    # Bar 2 - 2nd beat: F7
    pretty_midi.Note(velocity=110, pitch=53, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=110, pitch=57, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=110, pitch=60, start=2.25, end=2.625),  # C
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.625),  # D
    # Bar 2 - 4th beat: F7
    pretty_midi.Note(velocity=110, pitch=53, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=110, pitch=57, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=110, pitch=60, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=110, pitch=62, start=3.375, end=3.75),  # D
    # Bar 3 - 2nd beat: F7
    pretty_midi.Note(velocity=110, pitch=53, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=110, pitch=57, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=110, pitch=60, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=110, pitch=62, start=4.875, end=5.25),  # D
    # Bar 3 - 4th beat: F7
    pretty_midi.Note(velocity=110, pitch=53, start=5.625, end=6.0),  # F
    pretty_midi.Note(velocity=110, pitch=57, start=5.625, end=6.0),  # A
    pretty_midi.Note(velocity=110, pitch=60, start=5.625, end=6.0),  # C
    pretty_midi.Note(velocity=110, pitch=62, start=5.625, end=6.0),  # D
]
piano.notes.extend(piano_notes)

# Drums: Bars 2-4
drum_notes_bars2_4 = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=2.25),  # Hihat on 1 & 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=3.0),  # Hihat on 3 & 4
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.75),  # Hihat on 1 & 2
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.5),  # Hihat on 3 & 4
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=5.25),  # Hihat on 1 & 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=6.0),  # Hihat on 3 & 4
]
drums.notes.extend(drum_notes_bars2_4)

# Saxophone (Dante) - Melody
# Bar 2: Start the motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=110, pitch=64, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=110, pitch=65, start=2.25, end=2.625),  # Bb
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=110, pitch=64, start=3.375, end=3.75),  # A
    # Bar 4: Come back and finish it
    pretty_midi.Note(velocity=110, pitch=65, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=110, pitch=67, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=110, pitch=69, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=110, pitch=71, start=5.625, end=6.0),  # E
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
