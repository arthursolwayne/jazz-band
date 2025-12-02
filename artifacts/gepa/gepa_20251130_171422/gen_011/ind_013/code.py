
import pretty_midi

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set key to D major (key number 2)
pm.key_signature = pretty_midi.KeySignature(key_number=2)

# Create instruments
drums = pretty_midi.Instrument(program=10)  # Drums (program 10)
bass = pretty_midi.Instrument(program=33)    # Upright Bass (program 33)
piano = pretty_midi.Instrument(program=0)    # Acoustic Piano (program 0)
sax = pretty_midi.Instrument(program=64)     # Tenor Sax (program 64)

# Add instruments to the MIDI file
pm.instruments.append(drums)
pm.instruments.append(bass)
pm.instruments.append(piano)
pm.instruments.append(sax)

# Define note durations and timing (160 BPM => 0.375 seconds per beat)
beat = 0.375
bar = 4 * beat  # 1.5 seconds per bar

# Bar 1: Little Ray on drums (Kick on 1 and 3, Snare on 2 and 4, Hihat on every eighth)
# Time: 0.0 to 1.5 seconds
for i in range(0, 4):
    time = i * beat
    # Kick on 1 and 3
    if i % 2 == 0:
        kick = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1)
        drums.notes.append(kick)
    # Snare on 2 and 4
    if i % 2 == 1:
        snare = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.1)
        drums.notes.append(snare)
    # Hihat on every eighth
    hihat = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.1)
    drums.notes.append(hihat)

# Bar 2-4: All instruments in. Sax takes the melody.

# Define sax melody (D major, motif that starts, leaves a space, then returns)
# D (D4) -> F# (F#4) -> G (G4) -> A (A4)
# Then wait a moment (space), then return to D (D4) -> F# (F#4) -> G (G4)
# Total: 1.5 seconds per bar, so 4 bars = 6 seconds

sax_notes = [
    # Bar 2: D4, F#4, G4, A4
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=66, start=1.75, end=2.0),
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.5),

    # Bar 3: Rest (space)
    # No notes

    # Bar 4: Return with D4, F#4, G4
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=66, start=3.25, end=3.5),
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75),
]

sax.notes.extend(sax_notes)

# Bass line: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    # Bar 2: D (D3) -> C# (C#3) -> D (D3) -> E (E3)
    pretty_midi.Note(velocity=80, pitch=50, start=1.5, end=1.75),
    pretty_midi.Note(velocity=80, pitch=49, start=1.75, end=2.0),
    pretty_midi.Note(velocity=80, pitch=50, start=2.0, end=2.25),
    pretty_midi.Note(velocity=80, pitch=52, start=2.25, end=2.5),

    # Bar 3: F# (F#3) -> G (G3) -> A (A3) -> B (B3)
    pretty_midi.Note(velocity=80, pitch=53, start=2.5, end=2.75),
    pretty_midi.Note(velocity=80, pitch=55, start=2.75, end=3.0),
    pretty_midi.Note(velocity=80, pitch=57, start=3.0, end=3.25),
    pretty_midi.Note(velocity=80, pitch=59, start=3.25, end=3.5),

    # Bar 4: D (D3) -> C# (C#3) -> D (D3) -> E (E3)
    pretty_midi.Note(velocity=80, pitch=50, start=3.5, end=3.75),
    pretty_midi.Note(velocity=80, pitch=49, start=3.75, end=4.0),
    pretty_midi.Note(velocity=80, pitch=50, start=4.0, end=4.25),
    pretty_midi.Note(velocity=80, pitch=52, start=4.25, end=4.5),
]

bass.notes.extend(bass_notes)

# Piano: Comp on 2 and 4 with 7th chords
# Bar 2: D7 (D, F#, A, C)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=66, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=69, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=60, start=1.75, end=2.0),

    # Bar 3: Rest (no comp)
    # No notes

    # Bar 4: D7 again
    pretty_midi.Note(velocity=90, pitch=62, start=3.5, end=3.75),
    pretty_midi.Note(velocity=90, pitch=66, start=3.5, end=3.75),
    pretty_midi.Note(velocity=90, pitch=69, start=3.5, end=3.75),
    pretty_midi.Note(velocity=90, pitch=60, start=3.5, end=3.75),
]

piano.notes.extend(piano_notes)

# Write the MIDI file to disk
pm.write("wayne_moment.mid")

print("MIDI file 'wayne_moment.mid' created successfully.")
