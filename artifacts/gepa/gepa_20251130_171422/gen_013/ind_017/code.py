
import pretty_midi
import numpy as np

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set key to F minor (Fm)
key_signature = pretty_midi.KeySignature(key_number=24)  # 24 = F minor
pm.key_signature = key_signature

# Create instruments
tenor_sax = pretty_midi.Instrument(program=64)  # Tenor sax
bass = pretty_midi.Instrument(program=33)  # Double bass
piano = pretty_midi.Instrument(program=0)    # Acoustic piano
drums = pretty_midi.Instrument(program=128)  # Drums

pm.instruments = [tenor_sax, bass, piano, drums]

# Time settings
BPM = 160
note_length = 60 / BPM  # 0.375 seconds per beat
bar_length = 4 * note_length  # 6 seconds per bar

# Bar 1: Drums only
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for beat in range(0, 4):
    time = beat * note_length
    if beat % 2 == 0:
        # Kick
        note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + note_length)
        drums.notes.append(note)
    else:
        # Snare
        note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + note_length)
        drums.notes.append(note)
    # Hi-Hat on every eighth
    for eighth in range(0, 2):
        note = pretty_midi.Note(velocity=70, pitch=42, start=time + eighth * note_length / 2, end=time + eighth * note_length / 2 + note_length / 4)
        drums.notes.append(note)

# Bar 2: Everyone enters
# Marcus: Walking bass line in Fm, chromatic approaches
bass_notes = [35, 33, 31, 29, 28, 30, 32, 34]  # Chromatic approach to Fm7
for i, pitch in enumerate(bass_notes):
    time = i * note_length
    note = pretty_midi.Note(velocity=75, pitch=pitch, start=time, end=time + note_length / 2)
    bass.notes.append(note)

# Diane: Piano comping on 2 and 4 with 7th chords
# Fm7 = F Ab C Eb (F7 is F A C Eb, but in Fm it's F Ab C Eb)
# 7th chords on 2 and 4 (beats 2 and 4)
for beat in [1, 3]:
    time = beat * note_length
    # Fm7
    for pitch in [76, 70, 69, 64]:  # F, Ab, C, Eb
        note = pretty_midi.Note(velocity=85, pitch=pitch, start=time, end=time + note_length)
        piano.notes.append(note)

# Bar 3: Tenor sax takes melody
# Melody: F Ab Bb C Eb (sax in Bb, F is written as C)
# But in the key of Fm, we’ll use chromatic tension
# Short motif: Start on Ab, move to C, then Eb — leave it hanging
tenor_notes = [
    (0, 69),  # Ab
    (note_length, 72),  # C
    (2 * note_length, 74),  # Eb
    (3 * note_length, 72)  # C (rest on final note)
]

for time, pitch in tenor_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + note_length)
    tenor_sax.notes.append(note)

# Bar 4: Continue the melody with a resolution and return
tenor_notes = [
    (0, 70),      # F
    (note_length, 69),  # Ab
    (2 * note_length, 72),  # C
    (3 * note_length, 70)  # F
]

for time, pitch in tenor_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + note_length)
    tenor_sax.notes.append(note)

# Re-add the piano comping on 2 and 4
for beat in [1, 3]:
    time = beat * note_length
    # Fm7
    for pitch in [76, 70, 69, 64]:  # F, Ab, C, Eb
        note = pretty_midi.Note(velocity=85, pitch=pitch, start=time, end=time + note_length)
        piano.notes.append(note)

# Re-add the bass line continuing the walking pattern
bass_notes = [34, 35, 33, 31, 29, 28, 30, 32]  # Chromatic approach to Fm7
for i, pitch in enumerate(bass_notes):
    time = (i + 4) * note_length
    note = pretty_midi.Note(velocity=75, pitch=pitch, start=time, end=time + note_length / 2)
    bass.notes.append(note)

# Re-add the drums
for beat in range(4, 8):
    time = beat * note_length
    if beat % 2 == 0:
        # Kick
        note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + note_length)
        drums.notes.append(note)
    else:
        # Snare
        note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + note_length)
        drums.notes.append(note)
    # Hi-Hat on every eighth
    for eighth in range(0, 2):
        note = pretty_midi.Note(velocity=70, pitch=42, start=time + eighth * note_length / 2, end=time + eighth * note_length / 2 + note_length / 4)
        drums.notes.append(note)

# Save the MIDI file
pm.write("dante_intro.mid")
print("MIDI file created: 'dante_intro.mid'")
