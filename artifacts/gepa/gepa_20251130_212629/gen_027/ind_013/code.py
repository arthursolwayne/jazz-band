
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.25),  # kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=0.25, end=0.5),  # hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.0),  # kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.0, end=1.5),   # hihat on 4
    pretty_midi.Note(velocity=100, pitch=36, start=1.25, end=1.5),  # kick on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Full ensemble (1.5 - 3.0s)

# Bass: Marcus - walking line with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=44, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=90, pitch=45, start=1.75, end=2.0),  # F#
    pretty_midi.Note(velocity=90, pitch=43, start=2.0, end=2.25),  # E
    pretty_midi.Note(velocity=90, pitch=41, start=2.25, end=2.5),  # D
]
bass.notes.extend(bass_notes)

# Piano: Diane - comping with 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=64, start=1.75, end=2.0),  # C (F7)
    pretty_midi.Note(velocity=90, pitch=69, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=90, pitch=62, start=1.75, end=2.0),  # E
    pretty_midi.Note(velocity=85, pitch=60, start=1.75, end=2.0),  # D

    pretty_midi.Note(velocity=95, pitch=64, start=2.5, end=2.75),  # C (F7)
    pretty_midi.Note(velocity=90, pitch=69, start=2.5, end=2.75),  # G
    pretty_midi.Note(velocity=90, pitch=62, start=2.5, end=2.75),  # E
    pretty_midi.Note(velocity=85, pitch=60, start=2.5, end=2.75),  # D
]
piano.notes.extend(piano_notes)

# Sax: Dante - motif, start it, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=105, pitch=65, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),  # D
]
sax.notes.extend(sax_notes)

# Drums: Bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.75),  # kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.75, end=2.0),  # snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=2.0),   # hihat on 1-2
    pretty_midi.Note(velocity=100, pitch=36, start=2.0, end=2.25),  # kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.5),  # snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=2.0, end=2.5),   # hihat on 3-4
]
drums.notes.extend(drum_notes)

# Bar 3: Full ensemble (3.0 - 4.5s)

# Bass: Marcus - walking line with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=41, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=90, pitch=42, start=3.25, end=3.5),  # D#
    pretty_midi.Note(velocity=90, pitch=43, start=3.5, end=3.75),  # E
    pretty_midi.Note(velocity=90, pitch=44, start=3.75, end=4.0),  # F
]
bass.notes.extend(bass_notes)

# Piano: Diane - comping with 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=64, start=3.25, end=3.5),  # C (F7)
    pretty_midi.Note(velocity=90, pitch=69, start=3.25, end=3.5),  # G
    pretty_midi.Note(velocity=90, pitch=62, start=3.25, end=3.5),  # E
    pretty_midi.Note(velocity=85, pitch=60, start=3.25, end=3.5),  # D

    pretty_midi.Note(velocity=95, pitch=64, start=4.0, end=4.25),  # C (F7)
    pretty_midi.Note(velocity=90, pitch=69, start=4.0, end=4.25),  # G
    pretty_midi.Note(velocity=90, pitch=62, start=4.0, end=4.25),  # E
    pretty_midi.Note(velocity=85, pitch=60, start=4.0, end=4.25),  # D
]
piano.notes.extend(piano_notes)

# Sax: Dante - continue motif, unresolved
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=105, pitch=67, start=3.25, end=3.5),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.0),  # F
]
sax.notes.extend(sax_notes)

# Drums: Bar 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.25),  # kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.25, end=3.5),  # snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.5),   # hihat on 1-2
    pretty_midi.Note(velocity=100, pitch=36, start=3.5, end=3.75),  # kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.0),  # snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=3.5, end=4.0),   # hihat on 3-4
]
drums.notes.extend(drum_notes)

# Bar 4: Full ensemble (4.5 - 6.0s)

# Bass: Marcus - walking line with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=44, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=90, pitch=45, start=4.75, end=5.0),  # F#
    pretty_midi.Note(velocity=90, pitch=43, start=5.0, end=5.25),  # E
    pretty_midi.Note(velocity=90, pitch=41, start=5.25, end=5.5),  # D
]
bass.notes.extend(bass_notes)

# Piano: Diane - comping with 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=64, start=4.75, end=5.0),  # C (F7)
    pretty_midi.Note(velocity=90, pitch=69, start=4.75, end=5.0),  # G
    pretty_midi.Note(velocity=90, pitch=62, start=4.75, end=5.0),  # E
    pretty_midi.Note(velocity=85, pitch=60, start=4.75, end=5.0),  # D

    pretty_midi.Note(velocity=95, pitch=64, start=5.5, end=5.75),  # C (F7)
    pretty_midi.Note(velocity=90, pitch=69, start=5.5, end=5.75),  # G
    pretty_midi.Note(velocity=90, pitch=62, start=5.5, end=5.75),  # E
    pretty_midi.Note(velocity=85, pitch=60, start=5.5, end=5.75),  # D
]
piano.notes.extend(piano_notes)

# Sax: Dante - motif variation, ends with a question
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=105, pitch=65, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5),  # D
]
sax.notes.extend(sax_notes)

# Drums: Bar 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.75),  # kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.75, end=5.0),  # snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=5.0),   # hihat on 1-2
    pretty_midi.Note(velocity=100, pitch=36, start=5.0, end=5.25),  # kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.5),  # snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=5.0, end=5.5),   # hihat on 3-4
]
drums.notes.extend(drum_notes)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save MIDI
midi.write("wayne_intro.mid")
