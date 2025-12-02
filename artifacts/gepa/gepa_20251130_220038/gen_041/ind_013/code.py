
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
    # Kick on 1 and 3
    pretty_midi.Note(velocity=80, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in D, chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.75),  # D3
    pretty_midi.Note(velocity=80, pitch=61, start=1.75, end=2.0),  # C#3
    pretty_midi.Note(velocity=80, pitch=63, start=2.0, end=2.25),  # D#3
    pretty_midi.Note(velocity=80, pitch=65, start=2.25, end=2.5),  # F#3
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=80, pitch=65, start=3.0, end=3.25),  # F#3
    pretty_midi.Note(velocity=80, pitch=64, start=3.25, end=3.5),  # G3
    pretty_midi.Note(velocity=80, pitch=62, start=3.5, end=3.75),  # D3
    pretty_midi.Note(velocity=80, pitch=63, start=3.75, end=4.0),  # D#3
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=80, pitch=63, start=4.5, end=4.75),  # D#3
    pretty_midi.Note(velocity=80, pitch=62, start=4.75, end=5.0),  # D3
    pretty_midi.Note(velocity=80, pitch=60, start=5.0, end=5.25),  # B2
    pretty_midi.Note(velocity=80, pitch=62, start=5.25, end=5.5),  # D3
    pretty_midi.Note(velocity=80, pitch=64, start=5.5, end=5.75),  # G3
    pretty_midi.Note(velocity=80, pitch=65, start=5.75, end=6.0),  # F#3
]
bass.notes.extend(bass_notes)

# Diane: Piano comping on 2 and 4 with 7th chords
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=80, pitch=67, start=1.75, end=2.0),  # A3 (D7 chord)
    pretty_midi.Note(velocity=80, pitch=69, start=1.75, end=2.0),  # B3
    pretty_midi.Note(velocity=80, pitch=71, start=1.75, end=2.0),  # D4
    pretty_midi.Note(velocity=80, pitch=74, start=1.75, end=2.0),  # F#4
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=80, pitch=67, start=3.25, end=3.5),  # A3 (D7 chord)
    pretty_midi.Note(velocity=80, pitch=69, start=3.25, end=3.5),  # B3
    pretty_midi.Note(velocity=80, pitch=71, start=3.25, end=3.5),  # D4
    pretty_midi.Note(velocity=80, pitch=74, start=3.25, end=3.5),  # F#4
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=80, pitch=67, start=5.0, end=5.25),  # A3 (D7 chord)
    pretty_midi.Note(velocity=80, pitch=69, start=5.0, end=5.25),  # B3
    pretty_midi.Note(velocity=80, pitch=71, start=5.0, end=5.25),  # D4
    pretty_midi.Note(velocity=80, pitch=74, start=5.0, end=5.25),  # F#4
]
piano.notes.extend(piano_notes)

# Dante: Tenor sax melody - whisper then cry
sax_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=60, pitch=65, start=1.5, end=1.75),  # F#3 (whisper)
    pretty_midi.Note(velocity=80, pitch=67, start=1.75, end=2.0),  # A3 (cry)
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=60, pitch=69, start=3.0, end=3.25),  # B3 (whisper)
    pretty_midi.Note(velocity=80, pitch=71, start=3.25, end=3.5),  # D4 (cry)
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=60, pitch=67, start=4.5, end=4.75),  # A3 (whisper)
    pretty_midi.Note(velocity=80, pitch=69, start=4.75, end=5.0),  # B3 (cry)
    pretty_midi.Note(velocity=60, pitch=71, start=5.0, end=5.25),  # D4 (whisper)
    pretty_midi.Note(velocity=80, pitch=74, start=5.25, end=5.5),  # F#4 (cry)
    pretty_midi.Note(velocity=60, pitch=71, start=5.5, end=5.75),  # D4 (whisper)
    pretty_midi.Note(velocity=80, pitch=67, start=5.75, end=6.0),  # A3 (cry)
]
sax.notes.extend(sax_notes)

# Drums: Bar 2 (3.0 - 4.5s)
drum_notes_bar2 = [
    pretty_midi.Note(velocity=80, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=3.875),  # Snare on 2
    pretty_midi.Note(velocity=80, pitch=36, start=4.125, end=4.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),  # Snare on 4
]
# Hihat on every eighth
for t in [3.0, 3.1875, 3.375, 3.5625, 3.75, 3.9375, 4.125, 4.3125, 4.5, 4.6875, 4.875, 5.0]:
    drum_notes_bar2.append(pretty_midi.Note(velocity=80, pitch=42, start=t, end=t + 0.1875))
drums.notes.extend(drum_notes_bar2)

# Drums: Bar 3 (4.5 - 6.0s)
drum_notes_bar3 = [
    pretty_midi.Note(velocity=80, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.375),  # Snare on 2
    pretty_midi.Note(velocity=80, pitch=36, start=5.625, end=6.0),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.125),  # Snare on 4
]
# Hihat on every eighth
for t in [4.5, 4.6875, 4.875, 5.0625, 5.25, 5.4375, 5.625, 5.8125, 6.0, 6.1875, 6.375, 6.5625]:
    drum_notes_bar3.append(pretty_midi.Note(velocity=80, pitch=42, start=t, end=t + 0.1875))
drums.notes.extend(drum_notes_bar3)

# Add instruments to the MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
