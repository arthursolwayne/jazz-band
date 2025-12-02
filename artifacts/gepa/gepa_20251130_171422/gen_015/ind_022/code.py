
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Create a mysterious, suspenseful rhythm
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75), # Hihat
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),  # Snare
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),  # Hihat
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# SAX: Start the motif (D, F#, A, B)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D5
    pretty_midi.Note(velocity=100, pitch=66, start=1.75, end=2.0),  # F#5
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.25),  # A5
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.5),  # B5
    pretty_midi.Note(velocity=100, pitch=66, start=2.5, end=2.75),  # F#5
    pretty_midi.Note(velocity=100, pitch=62, start=2.75, end=3.0),  # D5
]
sax.notes.extend(sax_notes)

# BASS: Walking line with chromatic passing tones
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=45, start=1.5, end=1.75),  # D3
    pretty_midi.Note(velocity=70, pitch=46, start=1.75, end=2.0),  # Eb3
    pretty_midi.Note(velocity=70, pitch=47, start=2.0, end=2.25),  # E3
    pretty_midi.Note(velocity=70, pitch=49, start=2.25, end=2.5),  # G3
    pretty_midi.Note(velocity=70, pitch=50, start=2.5, end=2.75),  # G#3
    pretty_midi.Note(velocity=70, pitch=52, start=2.75, end=3.0),  # A3
]
bass.notes.extend(bass_notes)

# PIANO: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.75),  # D5
    pretty_midi.Note(velocity=80, pitch=66, start=1.5, end=1.75),  # F#5
    pretty_midi.Note(velocity=80, pitch=69, start=1.5, end=1.75),  # A5
    pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=1.75),  # B5

    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.5),  # F#5
    pretty_midi.Note(velocity=80, pitch=71, start=2.25, end=2.5),  # B5
    pretty_midi.Note(velocity=80, pitch=74, start=2.25, end=2.5),  # D6
    pretty_midi.Note(velocity=80, pitch=76, start=2.25, end=2.5),  # E6
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# SAX: Repeat motif with slight variation
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # D5
    pretty_midi.Note(velocity=100, pitch=66, start=3.25, end=3.5),  # F#5
    pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=3.75),  # A5
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.0),  # B5
    pretty_midi.Note(velocity=100, pitch=66, start=4.0, end=4.25),  # F#5
    pretty_midi.Note(velocity=100, pitch=62, start=4.25, end=4.5),  # D5
]
sax.notes.extend(sax_notes)

# BASS: Walking line with chromatic passing tones
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=52, start=3.0, end=3.25),  # A3
    pretty_midi.Note(velocity=70, pitch=53, start=3.25, end=3.5),  # A#3
    pretty_midi.Note(velocity=70, pitch=55, start=3.5, end=3.75),  # C4
    pretty_midi.Note(velocity=70, pitch=57, start=3.75, end=4.0),  # D4
    pretty_midi.Note(velocity=70, pitch=58, start=4.0, end=4.25),  # D#4
    pretty_midi.Note(velocity=70, pitch=60, start=4.25, end=4.5),  # F4
]
bass.notes.extend(bass_notes)

# PIANO: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.25),  # F#5
    pretty_midi.Note(velocity=80, pitch=71, start=3.0, end=3.25),  # B5
    pretty_midi.Note(velocity=80, pitch=74, start=3.0, end=3.25),  # D6
    pretty_midi.Note(velocity=80, pitch=76, start=3.0, end=3.25),  # E6

    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.0),  # D5
    pretty_midi.Note(velocity=80, pitch=66, start=3.75, end=4.0),  # F#5
    pretty_midi.Note(velocity=80, pitch=69, start=3.75, end=4.0),  # A5
    pretty_midi.Note(velocity=80, pitch=71, start=3.75, end=4.0),  # B5
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# SAX: Repeat motif with dynamic drop and slight delay
sax_notes = [
    pretty_midi.Note(velocity=70, pitch=62, start=4.5, end=4.75),  # D5
    pretty_midi.Note(velocity=70, pitch=66, start=4.75, end=5.0),  # F#5
    pretty_midi.Note(velocity=70, pitch=69, start=5.0, end=5.25),  # A5
    pretty_midi.Note(velocity=70, pitch=71, start=5.25, end=5.5),  # B5
    pretty_midi.Note(velocity=70, pitch=66, start=5.5, end=5.75),  # F#5
    pretty_midi.Note(velocity=70, pitch=62, start=5.75, end=6.0),  # D5
]
sax.notes.extend(sax_notes)

# BASS: Walking line with chromatic passing tones
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=60, start=4.5, end=4.75),  # F4
    pretty_midi.Note(velocity=70, pitch=61, start=4.75, end=5.0),  # F#4
    pretty_midi.Note(velocity=70, pitch=63, start=5.0, end=5.25),  # G#4
    pretty_midi.Note(velocity=70, pitch=65, start=5.25, end=5.5),  # A#4
    pretty_midi.Note(velocity=70, pitch=66, start=5.5, end=5.75),  # B4
    pretty_midi.Note(velocity=70, pitch=68, start=5.75, end=6.0),  # C#5
]
bass.notes.extend(bass_notes)

# PIANO: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.75),  # D5
    pretty_midi.Note(velocity=80, pitch=66, start=4.5, end=4.75),  # F#5
    pretty_midi.Note(velocity=80, pitch=69, start=4.5, end=4.75),  # A5
    pretty_midi.Note(velocity=80, pitch=71, start=4.5, end=4.75),  # B5

    pretty_midi.Note(velocity=90, pitch=74, start=5.25, end=5.5),  # D6
    pretty_midi.Note(velocity=80, pitch=76, start=5.25, end=5.5),  # E6
    pretty_midi.Note(velocity=80, pitch=78, start=5.25, end=5.5),  # F#6
    pretty_midi.Note(velocity=80, pitch=81, start=5.25, end=5.5),  # A6
]
piano.notes.extend(piano_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75), # Snare
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75), # Hihat
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125), # Hihat
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # Snare
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),  # Hihat
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25), # Hihat
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),  # Snare
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),  # Hihat
    pretty_midi.Note(velocity=100, pitch=42, start=6.0, end=6.375),  # Hihat
]
drums.notes.extend(drum_notes)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
