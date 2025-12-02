
import pretty_midi

# Initialize a PrettyMIDI object with 160 BPM and D minor key
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define time signature: 4/4
time_signature = pretty_midi.TimeSignature(numerator=4, denominator=4, time=0)
midi.time_signature_changes.append(time_signature)

# Define key signature: Dm (two flats)
key_signature = pretty_midi.KeySignature(key_number=21, time=0)  # D minor
midi.key_signature_changes.append(key_signature)

# Define note durations in seconds (based on 160 BPM)
note_duration = 0.375  # 1/4 note

# Create instruments
drums = pretty_midi.Instrument(program=10)  # Drums
bass = pretty_midi.Instrument(program=33)    # Electric Bass
piano = pretty_midi.Instrument(program=0)   # Acoustic Piano
sax = pretty_midi.Instrument(program=64)    # Tenor Saxophone

# --- DRUMS (Bar 1: Little Ray alone) ---
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 1 = 0.0 to 1.5 seconds

# Kick on 1 (0.0) and 3 (0.75)
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.0 + note_duration))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=0.75 + note_duration))

# Snare on 2 (0.375) and 4 (1.125)
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.375 + note_duration))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.125 + note_duration))

# Hi-hat on every eighth (0.0, 0.375, 0.75, 1.125)
for t in [0.0, 0.375, 0.75, 1.125]:
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=t, end=t + note_duration / 4))

# --- BASS (Bars 2-4: Marcus on walking line with chromatic motion) ---
# Start at bar 2 (1.5 seconds)
# Chromatic walking line in Dm (D, Eb, E, F, F#, G, G#, A, Bb, B, C, C#, D...)

# D -> Eb -> E -> F -> F# -> G -> G# -> A -> Bb -> B -> C -> C# -> D
notes = [50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62]
note_on_times = [1.5, 1.875, 2.25, 2.625, 3.0, 3.375, 3.75, 4.125, 4.5, 4.875, 5.25, 5.625, 6.0]

for i in range(len(notes)):
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=notes[i], start=note_on_times[i], end=note_on_times[i] + note_duration))

# --- PIANO (Bars 2-4: Diane comping with 7th chords on 2 and 4) ---
# Dm7 = D, F, A, C (pitches 50, 53, 57, 60)
# Comp on 2 and 4 (1.875 and 4.125)

# 7th chord on beat 2 (bar 2)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=50, start=1.875, end=1.875 + note_duration))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=53, start=1.875, end=1.875 + note_duration))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=57, start=1.875, end=1.875 + note_duration))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=1.875 + note_duration))

# 7th chord on beat 4 (bar 2)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=50, start=4.125, end=4.125 + note_duration))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=53, start=4.125, end=4.125 + note_duration))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=57, start=4.125, end=4.125 + note_duration))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=4.125, end=4.125 + note_duration))

# --- SAX (Bars 2-4: Dante's motif — a three-note phrase, then a rest, then a resolution) ---
# Motif: Dm (50) -> F (53) -> Bb (58) — then rest for one beat, then D (50) again.

# Phrase 1: D -> F -> Bb
sax.notes.append(pretty_midi.Note(velocity=110, pitch=50, start=1.5, end=1.5 + note_duration))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=53, start=1.875, end=1.875 + note_duration))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=58, start=2.25, end=2.25 + note_duration))

# Rest for one beat (2.625 to 3.0)
# Then resolution on D (50)
sax.notes.append(pretty_midi.Note(velocity=110, pitch=50, start=3.0, end=3.0 + note_duration))

# Add instruments to the MIDI
midi.instruments.append(drums)
midi.instruments.append(bass)
midi.instruments.append(piano)
midi.instruments.append(sax)

# Save the MIDI file
midi.write("dante_intro.mid")
print("MIDI file saved as 'dante_intro.mid'")
