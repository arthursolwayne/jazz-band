
import pretty_midi
import numpy as np

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set the time signature (4/4)
pm.time_signature_changes[0].numerator = 4
pm.time_signature_changes[0].denominator = 4

# Set the key signature (D minor)
pm.key_signature_changes[0].key_number = 2  # D minor

# Define the duration of a beat in seconds
BPM = 160
beat_duration = 60.0 / BPM

# Create instruments
saxophone_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
piano_program = pretty_midi.instrument_name_to_program('Acoustic Piano')
drum_program = pretty_midi.instrument_name_to_program('Drums')

sax = pretty_midi.Instrument(program=saxophone_program)
bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
drums = pretty_midi.Instrument(program=drum_program)

pm.instruments = [sax, bass, piano, drums]

# ------------------------------ DRUMS ------------------------------
# Bar 1: Little Ray alone
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = {
    'kick': [0, 2, 3, 5],  # 1, 2, 3, 4
    'snare': [1, 3],       # 2, 4
    'hihat': [0, 1, 2, 3, 4, 5, 6, 7],  # every eighth note
}

# Assign drum note numbers
Kick = 36
Snare = 38
HiHat = 42

# Bar 1: Time = 0 to 1.5s
for i in drum_notes['hihat']:
    note = pretty_midi.Note(
        velocity=50,
        pitch=HiHat,
        start=i * beat_duration / 2,
        end=(i + 1) * beat_duration / 2
    )
    drums.notes.append(note)

for i in drum_notes['kick']:
    note = pretty_midi.Note(
        velocity=80,
        pitch=Kick,
        start=i * beat_duration / 2,
        end=(i + 1) * beat_duration / 2
    )
    drums.notes.append(note)

for i in drum_notes['snare']:
    note = pretty_midi.Note(
        velocity=90,
        pitch=Snare,
        start=i * beat_duration / 2,
        end=(i + 1) * beat_duration / 2
    )
    drums.notes.append(note)

# ------------------------------ PIANO (Bars 2-4) ------------------------------
# Diane: 7th chords, comp on 2 and 4. Use emotional dynamics
# Dm7 = D F A C (root, b3, 5, b7)
# Dm7 is the tonic chord in D minor

# Bar 2 (beat 2)
# Dm7: D, F, A, C
chord_notes = [62, 64, 67, 69]  # D, F, A, C
for note in chord_notes:
    piano_note = pretty_midi.Note(
        velocity=np.random.randint(80, 100),
        pitch=note,
        start=beat_duration * 1,  # beat 2 of bar 2
        end=beat_duration * 1 + beat_duration / 4
    )
    piano.notes.append(piano_note)

# Bar 3 (beat 2)
# Use a chromatic approach: C# (chromatic below D)
# Gm7 (ii chord): G, Bb, D, F
chord_notes = [67, 71, 69, 71]  # G, Bb, D, F
for note in chord_notes:
    piano_note = pretty_midi.Note(
        velocity=np.random.randint(80, 100),
        pitch=note,
        start=beat_duration * 3,  # beat 2 of bar 3
        end=beat_duration * 3 + beat_duration / 4
    )
    piano.notes.append(piano_note)

# Bar 4 (beat 2)
# Bb7 (V7): Bb, D, F, Ab
chord_notes = [71, 69, 71, 68]  # Bb, D, F, Ab
for note in chord_notes:
    piano_note = pretty_midi.Note(
        velocity=np.random.randint(80, 100),
        pitch=note,
        start=beat_duration * 5,  # beat 2 of bar 4
        end=beat_duration * 5 + beat_duration / 4
    )
    piano.notes.append(piano_note)

# ------------------------------ BASS (Bars 2-4) ------------------------------
# Marcus: Walking line, chromatic approaches, active and melodic

# Bar 2: Dm7
bass_notes = [62, 64, 66, 67]  # D, F, Eb, A
for note in bass_notes:
    bass_note = pretty_midi.Note(
        velocity=70,
        pitch=note,
        start=beat_duration * 1,
        end=beat_duration * 1 + beat_duration / 4
    )
    bass.notes.append(bass_note)

# Bar 3: Gm7 (ii chord)
bass_notes = [67, 71, 69, 67]  # G, Bb, D, G
for note in bass_notes:
    bass_note = pretty_midi.Note(
        velocity=70,
        pitch=note,
        start=beat_duration * 3,
        end=beat_duration * 3 + beat_duration / 4
    )
    bass.notes.append(bass_note)

# Bar 4: Bb7 (V7)
bass_notes = [71, 69, 71, 68]  # Bb, D, F, Ab
for note in bass_notes:
    bass_note = pretty_midi.Note(
        velocity=70,
        pitch=note,
        start=beat_duration * 5,
        end=beat_duration * 5 + beat_duration / 4
    )
    bass.notes.append(bass_note)

# ------------------------------ SAX (Bars 2-4) ------------------------------
# Your motif: short, emotional, memorable
# Start with a descending motif in Dm, then return and resolve

# Bar 2
# Motif: D -> C -> Bb -> A (melodic descent into the tonic)
sax_notes = [62, 60, 61, 67]  # D, C, Bb, A
for i, note in enumerate(sax_notes):
    sax_note = pretty_midi.Note(
        velocity=100,
        pitch=note,
        start=beat_duration * 1 + i * beat_duration / 4,
        end=beat_duration * 1 + (i + 1) * beat_duration / 4
    )
    sax.notes.append(sax_note)

# Bar 3
# Rest — let the tension build
# No notes played in bar 3

# Bar 4
# Return to the motif, but end on A (tonic of Dm)
sax_notes = [62, 60, 61, 67]  # D, C, Bb, A
for i, note in enumerate(sax_notes):
    sax_note = pretty_midi.Note(
        velocity=100,
        pitch=note,
        start=beat_duration * 5 + i * beat_duration / 4,
        end=beat_duration * 5 + (i + 1) * beat_duration / 4
    )
    sax.notes.append(sax_note)

# ------------------------------ Write to MIDI file ------------------------------
pm.write("dante_intro.mid")
print("MIDI file 'dante_intro.mid' created.")
