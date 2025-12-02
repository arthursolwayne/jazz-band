
import pretty_midi

# Initialize the MIDI file with tempo
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instruments
sax = pretty_midi.Instrument(program=66)       # Tenor sax
bass = pretty_midi.Instrument(program=33)      # Acoustic bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum notes: kick=36, snare=38, hihat=42
drum_notes = {
    'kick': 36,
    'snare': 38,
    'hihat': 42
}

# Time in seconds (bar = 1.5s, beat = 0.375s)
bar = 1.5
beat = 0.375
time = 0.0

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=drum_notes['kick'], start=time, end=time + beat))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=drum_notes['kick'], start=time + 2*beat, end=time + 2*beat + beat))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=drum_notes['snare'], start=time + beat, end=time + beat + beat))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=drum_notes['snare'], start=time + 3*beat, end=time + 3*beat + beat))

# Hihat on every eighth
for i in range(8):
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=drum_notes['hihat'], start=time + i * beat, end=time + i * beat + beat / 2))

time += bar

# Bar 2-4: Full quartet (1.5 - 6.0s)
# Key: F major (F, G, A, Bb, C, D, E)
# You (Dante) play a simple, haunting motif
# Melody: F - Bb - C - F (ascending, then resolving back)

# Sax: Tenor melody
note_durations = [0.5, 0.5, 0.5, 0.5]  # Each note is a half note
note_pitches = [77, 70, 72, 77]  # F, Bb, C, F (F4, Bb4, C5, F5)

for i, pitch in enumerate(note_pitches):
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=time + i * beat * 2, end=time + i * beat * 2 + note_durations[i] * beat * 2))

# Bass line: Marcus — walking line, chromatic approaches
# F - Eb - D - C (chromatic approach to F)
# F - G - A - Bb (F7 chord, walking)
# F - Eb - D - C (chromatic approach again)
# F - G - A - Bb (F7 chord, walking)

bass_notes = [76, 74, 73, 72, 76, 77, 78, 77, 76, 74, 73, 72, 76, 77, 78, 77]
bass_times = [0.0, 0.375, 0.75, 1.125, 1.5, 1.875, 2.25, 2.625, 3.0, 3.375, 3.75, 4.125, 4.5, 4.875, 5.25, 5.625]

for i, pitch in enumerate(bass_notes):
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=time + bass_times[i], end=time + bass_times[i] + beat / 2))

# Piano: Diane — 7th chords, comp on 2 and 4
# F7 (F, A, C, Eb) on beat 2 and 4 of each bar
chord_notes = [76, 78, 72, 74]  # F, A, C, Eb

# Bar 2: Time = 1.5s
piano.notes.append(pretty_midi.Note(velocity=100, pitch=76, start=time + beat, end=time + beat + beat / 2))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=78, start=time + beat, end=time + beat + beat / 2))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=time + beat, end=time + beat + beat / 2))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=time + beat, end=time + beat + beat / 2))

# Bar 3: Time = 3.0s
piano.notes.append(pretty_midi.Note(velocity=100, pitch=76, start=time + 3.0 + beat, end=time + 3.0 + beat + beat / 2))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=78, start=time + 3.0 + beat, end=time + 3.0 + beat + beat / 2))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=time + 3.0 + beat, end=time + 3.0 + beat + beat / 2))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=time + 3.0 + beat, end=time + 3.0 + beat + beat / 2))

# Bar 4: Time = 4.5s
piano.notes.append(pretty_midi.Note(velocity=100, pitch=76, start=time + 4.5 + beat, end=time + 4.5 + beat + beat / 2))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=78, start=time + 4.5 + beat, end=time + 4.5 + beat + beat / 2))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=time + 4.5 + beat, end=time + 4.5 + beat + beat / 2))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=time + 4.5 + beat, end=time + 4.5 + beat + beat / 2))

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Write the MIDI file
midi.write("dante_intro.mid")
