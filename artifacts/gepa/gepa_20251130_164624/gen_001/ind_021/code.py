
import pretty_midi

# Set tempo and time signature
tempo = 160  # BPM
time_signature = (4, 4)

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=tempo, time_signature=(4, 4))

# Set the key as D major
key = 'D'

# Define the duration of a beat in seconds
beat = 60.0 / tempo  # 0.375 seconds per beat
bar_length = 4 * beat  # 1.5 seconds per bar (4 beats)

# Define MIDI programs for each instrument
programs = {
    'tenor_sax': 64,  # Tenor saxophone
    'bass': 33,        # Upright bass
    'piano': 0,        # Acoustic piano
    'drums': 0         # Acoustic grand piano (for percussion)
}

# Create instrument tracks
tenor_sax = pretty_midi.Instrument(program=programs['tenor_sax'])
bass = pretty_midi.Instrument(program=programs['bass'])
piano = pretty_midi.Instrument(program=programs['piano'])
drums = pretty_midi.Instrument(program=programs['drums'])

# Add instruments to the PrettyMIDI object
pm.instruments.append(tenor_sax)
pm.instruments.append(bass)
pm.instruments.append(piano)
pm.instruments.append(drums)

# Define note values for each instrument
# 1. Drums - Bar 1: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = {
    'kick': 36,
    'snare': 38,
    'hihat': 42
}

for bar in range(1):
    # Bar 1: Just drums
    # Kick on 1 and 3
    kick_start = bar * bar_length
    kick = pretty_midi.Note(velocity=90, pitch=drum_notes['kick'], start=kick_start, end=kick_start + beat)
    drums.notes.append(kick)

    kick = pretty_midi.Note(velocity=90, pitch=drum_notes['kick'], start=kick_start + 2 * beat, end=kick_start + 3 * beat)
    drums.notes.append(kick)

    # Snare on 2 and 4
    snare = pretty_midi.Note(velocity=100, pitch=drum_notes['snare'], start=kick_start + beat, end=kick_start + 2 * beat)
    drums.notes.append(snare)

    snare = pretty_midi.Note(velocity=100, pitch=drum_notes['snare'], start=kick_start + 3 * beat, end=kick_start + 4 * beat)
    drums.notes.append(snare)

    # Hihat on every eighth
    for i in range(8):
        note_start = kick_start + (i * beat / 2)
        hihat = pretty_midi.Note(velocity=80, pitch=drum_notes['hihat'], start=note_start, end=note_start + beat / 2)
        drums.notes.append(hihat)

# 2. Bass - Chromatic walking line, no repeating notes
# Bar 2: start from D, chromatic up to F#, then back
bass_notes = [
    # Bar 2
    (62, 0.0), (63, 0.375), (64, 0.75), (65, 1.125), (66, 1.5), (67, 1.875), (68, 2.25), (69, 2.625)
]

# Bar 3: D, E, F#, G, A, B, C#, D
bass_notes.extend([
    (62, 3.0), (64, 3.375), (66, 3.75), (67, 4.125), (69, 4.5), (71, 4.875), (72, 5.25), (62, 5.625)
])

# Bar 4: start from D, chromatic up again
bass_notes.extend([
    (62, 6.0), (63, 6.375), (64, 6.75), (65, 7.125), (66, 7.5), (67, 7.875), (68, 8.25), (69, 8.625)
])

for pitch, start in bass_notes:
    bass_note = pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=start + beat / 2)
    bass.notes.append(bass_note)

# 3. Piano - 7th chords, comp on 2 and 4
# D7 = D, F#, A, C
# G7 = G, B, D, F
# C7 = C, E, G, B
# F7 = F, A, C, E

# Bar 2: D7 on beat 2
piano_notes = [
    # Bar 2, beat 2: D7
    (62, 1.5, 100), (66, 1.5, 100), (69, 1.5, 100), (64, 1.5, 100),

    # Bar 3, beat 4: G7
    (67, 4.5, 100), (71, 4.5, 100), (69, 4.5, 100), (66, 4.5, 100),

    # Bar 4, beat 2: C7
    (60, 3.0, 100), (64, 3.0, 100), (67, 3.0, 100), (71, 3.0, 100),

    # Bar 4, beat 4: F7
    (65, 4.5, 100), (69, 4.5, 100), (64, 4.5, 100), (67, 4.5, 100)
]

for pitch, start, velocity in piano_notes:
    piano_note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + beat / 2)
    piano.notes.append(piano_note)

# 4. Tenor Sax - Your motif: A short, singular phrase that sings
# Bar 2: A simple motif with rests
# D, E, F#, D (with rests in between to make it sing)
# Start at bar 2 (start = 1.5s), with a rest before

tenor_notes = [
    # Bar 2, beat 1: D (rest before, start at 1.5)
    (62, 1.5, 100, 0.5),
    # Bar 2, beat 2: E (start at 2.0)
    (64, 2.0, 100, 0.5),
    # Bar 2, beat 3: F# (start at 2.5)
    (66, 2.5, 100, 0.5),
    # Bar 2, beat 4: D (end at 3.0, but leave it hanging)
    (62, 3.0, 100, 0.0)
]

for pitch, start, velocity, duration in tenor_notes:
    tenor_note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + duration)
    tenor_sax.notes.append(tenor_note)

# Write the MIDI file to disk
pm.write('dante_introduction.mid')

print("MIDI file 'dante_introduction.mid' has been created successfully.")
