
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
    pretty_midi.Note(velocity=80, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),  # Hihat on 1
    pretty_midi.Note(velocity=80, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125), # Hihat on 2
    pretty_midi.Note(velocity=80, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),  # Hihat on 3
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875)   # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line, chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=43, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=44, start=1.875, end=2.25), # F#
    pretty_midi.Note(velocity=80, pitch=45, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),  # E

    # Bar 3
    pretty_midi.Note(velocity=80, pitch=41, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75), # E
    pretty_midi.Note(velocity=80, pitch=44, start=3.75, end=4.125), # F#
    pretty_midi.Note(velocity=80, pitch=45, start=4.125, end=4.5),  # G

    # Bar 4
    pretty_midi.Note(velocity=80, pitch=46, start=4.5, end=4.875),  # G#
    pretty_midi.Note(velocity=80, pitch=47, start=4.875, end=5.25), # A
    pretty_midi.Note(velocity=80, pitch=45, start=5.25, end=5.625), # G
    pretty_midi.Note(velocity=80, pitch=43, start=5.625, end=6.0),  # F
]
bass.notes.extend(bass_notes)

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=53, start=1.875, end=2.25),  # B7 (F7)
    pretty_midi.Note(velocity=90, pitch=45, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=90, pitch=47, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=90, pitch=50, start=1.875, end=2.25),  # C

    # Bar 3
    pretty_midi.Note(velocity=90, pitch=53, start=3.75, end=4.125),  # B7 (F7)
    pretty_midi.Note(velocity=90, pitch=45, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=90, pitch=47, start=3.75, end=4.125),  # A
    pretty_midi.Note(velocity=90, pitch=50, start=3.75, end=4.125),  # C

    # Bar 4
    pretty_midi.Note(velocity=90, pitch=53, start=5.25, end=5.625),  # B7 (F7)
    pretty_midi.Note(velocity=90, pitch=45, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=90, pitch=47, start=5.25, end=5.625),  # A
    pretty_midi.Note(velocity=90, pitch=50, start=5.25, end=5.625),  # C
]
piano.notes.extend(piano_notes)

# Sax (Dante): Whisper to cry
sax_notes = [
    pretty_midi.Note(velocity=60, pitch=62, start=1.5, end=1.75),  # A (F7)
    pretty_midi.Note(velocity=60, pitch=64, start=1.75, end=2.0),   # Bb (F7)
    pretty_midi.Note(velocity=60, pitch=65, start=2.0, end=2.25),  # B (F7)
    pretty_midi.Note(velocity=60, pitch=62, start=2.25, end=2.5),  # A (F7)
    pretty_midi.Note(velocity=80, pitch=67, start=2.5, end=2.75),  # D (F7)
    pretty_midi.Note(velocity=80, pitch=69, start=2.75, end=3.0),  # E (F7)
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.25),  # D (F7)
    pretty_midi.Note(velocity=80, pitch=65, start=3.25, end=3.5),  # B (F7)
    pretty_midi.Note(velocity=80, pitch=69, start=3.5, end=3.75),  # E (F7)
    pretty_midi.Note(velocity=80, pitch=67, start=3.75, end=4.0),  # D (F7)
    pretty_midi.Note(velocity=80, pitch=65, start=4.0, end=4.25),  # B (F7)
    pretty_midi.Note(velocity=80, pitch=62, start=4.25, end=4.5),  # A (F7)
    pretty_midi.Note(velocity=80, pitch=64, start=4.5, end=4.75),  # Bb (F7)
    pretty_midi.Note(velocity=80, pitch=65, start=4.75, end=5.0),  # B (F7)
    pretty_midi.Note(velocity=80, pitch=64, start=5.0, end=5.25),  # Bb (F7)
    pretty_midi.Note(velocity=80, pitch=62, start=5.25, end=5.5),  # A (F7)
    pretty_midi.Note(velocity=80, pitch=60, start=5.5, end=5.75),  # G (F7)
    pretty_midi.Note(velocity=80, pitch=62, start=5.75, end=6.0),  # A (F7)
]
sax.notes.extend(sax_notes)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
