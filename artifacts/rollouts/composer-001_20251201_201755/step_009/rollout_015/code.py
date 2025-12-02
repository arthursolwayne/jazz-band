
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.75),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.5),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax motif: F# - D - B - E (D minor scale, but with tension)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.75),  # F#
    pretty_midi.Note(velocity=100, pitch=59, start=1.75, end=2.0),  # D
    pretty_midi.Note(velocity=100, pitch=61, start=2.0, end=2.25),  # B
    pretty_midi.Note(velocity=100, pitch=63, start=2.25, end=2.5),  # E
]
sax.notes.extend(sax_notes)

# Bass: D2 (MIDI 38) walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.75),  # D2
    pretty_midi.Note(velocity=100, pitch=40, start=1.75, end=2.0),  # Eb2
    pretty_midi.Note(velocity=100, pitch=41, start=2.0, end=2.25),  # E2
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.5),  # D2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.0),  # Dm7: F# (62)
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.0),  # A (67)
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=2.0),  # D (72)
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.0),  # F (69)
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.5),  # Dm7: F# (62)
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.5),  # A (67)
    pretty_midi.Note(velocity=100, pitch=72, start=2.0, end=2.5),  # D (72)
    pretty_midi.Note(velocity=100, pitch=74, start=2.0, end=2.5),  # F# (74) - resolution
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Repeat the motif but with a slight variation
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.25),  # F#
    pretty_midi.Note(velocity=100, pitch=59, start=3.25, end=3.5),  # D
    pretty_midi.Note(velocity=100, pitch=61, start=3.5, end=3.75),  # B
    pretty_midi.Note(velocity=100, pitch=63, start=3.75, end=4.0),  # E
]
sax.notes.extend(sax_notes)

# Bass: D2 (MIDI 38) walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.25),  # D2
    pretty_midi.Note(velocity=100, pitch=40, start=3.25, end=3.5),  # Eb2
    pretty_midi.Note(velocity=100, pitch=41, start=3.5, end=3.75),  # E2
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.0),  # D2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.5),  # Dm7: F# (62)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.5),  # A (67)
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.5),  # D (72)
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.5),  # F (69)
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=4.0),  # Dm7: F# (62)
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=4.0),  # A (67)
    pretty_midi.Note(velocity=100, pitch=72, start=3.5, end=4.0),  # D (72)
    pretty_midi.Note(velocity=100, pitch=74, start=3.5, end=4.0),  # F# (74) - resolution
]
piano.notes.extend(piano_notes)

# Drums: Fill the bar
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.75),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.5),
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: End the motif with a strong note
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.75),  # F#
    pretty_midi.Note(velocity=100, pitch=59, start=4.75, end=5.0),  # D
    pretty_midi.Note(velocity=100, pitch=61, start=5.0, end=5.25),  # B
    pretty_midi.Note(velocity=100, pitch=63, start=5.25, end=5.5),  # E
    pretty_midi.Note(velocity=100, pitch=64, start=5.5, end=6.0),  # F# - hold
]
sax.notes.extend(sax_notes)

# Bass: D2 (MIDI 38) walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.75),  # D2
    pretty_midi.Note(velocity=100, pitch=40, start=4.75, end=5.0),  # Eb2
    pretty_midi.Note(velocity=100, pitch=41, start=5.0, end=5.25),  # E2
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.5),  # D2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=5.0),  # Dm7: F# (62)
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=5.0),  # A (67)
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=5.0),  # D (72)
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=5.0),  # F (69)
    pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.5),  # Dm7: F# (62)
    pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.5),  # A (67)
    pretty_midi.Note(velocity=100, pitch=72, start=5.0, end=5.5),  # D (72)
    pretty_midi.Note(velocity=100, pitch=74, start=5.0, end=5.5),  # F# (74) - resolution
]
piano.notes.extend(piano_notes)

# Drums: Fill the bar
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=5.25),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.75),
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
