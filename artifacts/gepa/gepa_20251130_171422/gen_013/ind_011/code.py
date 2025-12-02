
import pretty_midi
import numpy as np

# Create a new Pretty MIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set the time signature to 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Set the key signature to D minor (1 flat)
pm.key_signature_changes = [pretty_midi.KeySignature(5, 0)]  # D minor = 5th key in chromatic scale (C major is 0)

# Define the time per bar in seconds (at 160 BPM, each beat is 0.375 seconds)
time_per_beat = 60.0 / 160
time_per_bar = 4 * time_per_beat  # 1.5 seconds per bar

# Define the note durations and velocities
note_duration = time_per_beat / 2  # 1/8 note duration
velocity = 100  # moderate volume

# Instrument Channels
# -------------------
# 0: Drums (Little Ray)
# 1: Bass (Marcus)
# 2: Piano (Diane)
# 3: Tenor Sax (You)

# Create instruments
drum_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')  # Use piano for drum sounds (we'll use note numbers)
bass_program = pretty_midi.instrument_name_to_program('Fretless Bass')
piano_program = pretty_midi.instrument_name_to_program('Electric Piano 1')
sax_program = pretty_midi.instrument_name_to_program('Tenor Sax')

# Add instruments to the MIDI file
drums = pretty_midi.Instrument(program=drum_program)
bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
sax = pretty_midi.Instrument(program=sax_program)

pm.instruments.append(drums)
pm.instruments.append(bass)
pm.instruments.append(piano)
pm.instruments.append(sax)

# BAR 1: Little Ray (Drums) - Set it up
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Define MIDI note numbers for drum kit (Simplified)
KICK = 36
SNARE = 38
HIHAT = 42

# Bar 1 (0 to 1.5 seconds)
time = 0.0

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=time, end=time + note_duration))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=time + 2 * note_duration, end=time + 3 * note_duration))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=SNARE, start=time + note_duration, end=time + 2 * note_duration))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=SNARE, start=time + 3 * note_duration, end=time + 4 * note_duration))

# Hi-Hat on every eighth
for i in range(8):
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=HIHAT, start=time + i * note_duration, end=time + (i + 1) * note_duration))

# BAR 2: Everyone in. You take the melody.

# Diane (Piano) - 7th chords, comp on 2 and 4
# Dm7 = D, F, A, C
# Bbm7 = Bb, Db, F, Ab (to create a chromatic approach)
# Comp on 2 and 4 (Beat 2 and 4)

# Dm7 on beat 1
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=time + 0 * note_duration, end=time + note_duration))  # D4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=time + 0 * note_duration, end=time + note_duration))  # F4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=time + 0 * note_duration, end=time + note_duration))  # A4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=time + 0 * note_duration, end=time + note_duration))  # C5

# Bbm7 on beat 2
piano.notes.append(pretty_midi.Note(velocity=90, pitch=60, start=time + 1 * note_duration, end=time + 2 * note_duration))  # Bb4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=time + 1 * note_duration, end=time + 2 * note_duration))  # Db5
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=time + 1 * note_duration, end=time + 2 * note_duration))  # F5
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=time + 1 * note_duration, end=time + 2 * note_duration))  # Ab5

# Dm7 on beat 3 (but only root and 7th for space)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=time + 2 * note_duration, end=time + 3 * note_duration))  # D4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=time + 2 * note_duration, end=time + 3 * note_duration))  # C5

# Bbm7 on beat 4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=60, start=time + 3 * note_duration, end=time + 4 * note_duration))  # Bb4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=time + 3 * note_duration, end=time + 4 * note_duration))  # Db5
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=time + 3 * note_duration, end=time + 4 * note_duration))  # F5
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=time + 3 * note_duration, end=time + 4 * note_duration))  # Ab5

# Marcus (Bass) - Walking line, chromatic approaches, no repeats
# Dm7 -> Bbm7 -> Dm7 -> Bbm7

# Dm7 root and chromatic approach
# D -> C -> D -> F
bass.notes.append(pretty_midi.Note(velocity=80, pitch=62, start=time + 0 * note_duration, end=time + note_duration))  # D4
bass.notes.append(pretty_midi.Note(velocity=80, pitch=60, start=time + note_duration, end=time + 2 * note_duration))  # C4
bass.notes.append(pretty_midi.Note(velocity=80, pitch=62, start=time + 2 * note_duration, end=time + 3 * note_duration))  # D4
bass.notes.append(pretty_midi.Note(velocity=80, pitch=64, start=time + 3 * note_duration, end=time + 4 * note_duration))  # F4

# You (Tenor Sax) - Short motif, make it sing. Start it, leave it hanging. Come back and finish it.

# Dm scale: D, Eb, F, G, A, Bb, C
# Motif: D - F - Bb (suspense) - D (resolution)

# Bar 2: Start the motif
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=time + 0 * note_duration, end=time + note_duration))  # D4
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=time + note_duration, end=time + 2 * note_duration))  # F4
sax.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=time + 2 * note_duration, end=time + 3 * note_duration))  # Bb4

# Bar 3: Leave it hanging
# No notes from sax on bar 3 (space creates tension)

# Bar 4: Resolve it
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=time + 3 * note_duration, end=time + 4 * note_duration))  # D4

# Save the MIDI file
pm.write("dante_intro.mid")
print("MIDI file saved as 'dante_intro.mid'")
