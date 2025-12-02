
import pretty_midi

# Initialize the MIDI file with 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments
sax = pretty_midi.Instrument(program=66)       # Tenor sax
bass = pretty_midi.Instrument(program=33)      # Double bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# MIDI note numbers
# Drums
KICK = 36
SNARE = 38
HIHAT = 42

# Dm7 chord: D, F, A, C
Dm7 = [50, 53, 57, 60]

# Sax motif (Dm7 scale, but with a twist — question, not resolution)
sax_notes = [50, 53, 57, 60, 57, 53, 50, 50]  # D, F, A, C, A, F, D, D (leaves it hanging)
sax_velocity = [100, 100, 100, 100, 100, 100, 100, 80]  # Slight decrescendo on last note

# Bass line (chromatic walking, Dm7 context)
# 1: D, 2: Eb, 3: E, 4: F, 5: F#, 6: G, 7: G#, 8: A
bass_notes = [50, 51, 52, 53, 54, 55, 56, 57]
bass_velocity = [90] * 8
bass_time = [0.0, 0.375, 0.75, 1.125, 1.5, 1.875, 2.25, 2.625]  # every beat

# Piano: 7th chords on 2 and 4, Dm7, F7, A7, C7
piano_notes = [
    [],  # Bar 1 (no piano)
    [50, 53, 57, 60],  # Dm7 on beat 2
    [55, 57, 62, 67],  # F7 on beat 4
    [57, 60, 64, 69],  # A7 on beat 2
    [60, 62, 67, 72],  # C7 on beat 4
]
piano_velocity = [90] * 4

# Drums: Bar 1 only (1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [KICK, SNARE, HIHAT, KICK, SNARE, HIHAT]
drum_times = [0.0, 0.375, 0.75, 1.125, 1.5, 1.875]
drum_velocities = [100, 100, 80] * 2

# Add drum notes to the drum instrument
for note, time, vel in zip(drum_notes, drum_times, drum_velocities):
    drum_note = pretty_midi.Note(velocity=vel, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(drum_note)

# Bars 2-4 (1.5s to 6.0s)
# Sax: play the motif starting at 1.5s
for i, note in enumerate(sax_notes):
    time = 1.5 + i * 0.375
    sax_note = pretty_midi.Note(velocity=sax_velocity[i], pitch=note, start=time, end=time + 0.25)
    sax.notes.append(sax_note)

# Bass: play walking line starting at 1.5s
for i, note in enumerate(bass_notes):
    time = 1.5 + bass_time[i]
    bass_note = pretty_midi.Note(velocity=bass_velocity[i], pitch=note, start=time, end=time + 0.25)
    bass.notes.append(bass_note)

# Piano: play chords on beats 2 and 4 of bars 2 and 3
for i, notes in enumerate(piano_notes[1:]):  # skip 1st bar
    bar_time = 1.5 + i * 1.5  # bar 2, 3
    for j, note in enumerate(notes):
        time = bar_time + (j * 0.5)  # on 2 and 4 (0.5 and 1.0 seconds into the bar)
        piano_note = pretty_midi.Note(velocity=piano_velocity[j], pitch=note, start=time, end=time + 0.125)
        piano.notes.append(piano_note)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_cellar_intro.mid")
