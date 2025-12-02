
import pretty_midi
from pretty_midi import Note, Instrument, Program

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Time signature: 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Key: F Major
pm.key_signature_changes = [pretty_midi.KeySignature(5, 0)]  # F major is key number 5

# Create instruments
bass = Instrument(program=Program.BASS_GUITAR_FINGER_STYLE)
piano = Instrument(program=Program.ELECTRIC_PIANO_1)
drums = Instrument(program=Program.DRUMS)
sax = Instrument(program=Program.TENOR_SAX)

pm.instruments = [bass, piano, drums, sax]

# Time per bar in seconds (160 BPM, 4/4)
time_per_beat = 60.0 / 160
time_per_bar = time_per_beat * 4

# Bar 1: Little Ray — drums only
# Kick on 1 & 3, snare on 2 & 4, hihat on every 8th
# Time: bar starts at 0, lasts 6 seconds

for bar in range(1):
    bar_start = bar * time_per_bar
    # Kick on beat 0 and 2
    for beat in [0, 2]:
        beat_time = bar_start + beat * time_per_beat
        note_kick = Note(36, 100, beat_time, beat_time + 0.1)
        drums.notes.append(note_kick)
    # Snare on beat 1 and 3
    for beat in [1, 3]:
        beat_time = bar_start + beat * time_per_beat
        note_snare = Note(38, 100, beat_time, beat_time + 0.1)
        drums.notes.append(note_snare)
    # Hi-hat on every 8th
    for i in range(8):
        time = bar_start + (i * time_per_beat / 2)
        note_hihat = Note(42, 80, time, time + 0.05)
        drums.notes.append(note_hihat)

# Bar 2: Everyone comes in

# Marcus (bass) — walking line, chromatic approaches, never the same note twice
# F major scale: F, G, A, Bb, B, C, D
bass_notes = [
    Note(65, 60, 6.0, 6.2),  # F (beat 1)
    Note(67, 60, 6.2, 6.4),  # G (beat 2)
    Note(69, 60, 6.4, 6.6),  # A (beat 3)
    Note(66, 60, 6.6, 6.8),  # Bb (beat 4)
    Note(67, 60, 6.8, 7.0),  # G (beat 1 next bar)
]

for note in bass_notes:
    bass.notes.append(note)

# Diane (piano) — 7th chords, comp on 2 and 4
# F7 = F, A, C, Eb
# Bar 2: on beat 2
note_f = Note(65, 85, 6.2, 6.4)
note_a = Note(68, 85, 6.2, 6.4)
note_c = Note(69, 85, 6.2, 6.4)
note_eb = Note(67, 85, 6.2, 6.4)

for note in [note_f, note_a, note_c, note_eb]:
    piano.notes.append(note)

# Bar 3: Diane plays C7 on beat 2 (II chord)
note_c = Note(67, 85, 7.2, 7.4)
note_e = Note(69, 85, 7.2, 7.4)
note_g = Note(71, 85, 7.2, 7.4)
note_b = Note(73, 85, 7.2, 7.4)

for note in [note_c, note_e, note_g, note_b]:
    piano.notes.append(note)

# Bar 4: Diane plays Bb7 on beat 2 (V chord)
note_bb = Note(66, 85, 8.2, 8.4)
note_d = Note(68, 85, 8.2, 8.4)
note_f = Note(70, 85, 8.2, 8.4)
note_ab = Note(65, 85, 8.2, 8.4)

for note in [note_bb, note_d, note_f, note_ab]:
    piano.notes.append(note)

# Bar 2-4: You (sax) — sparse melody, one short motif
# F, Bb, C, F — sparse and expressive
# Bar 2: F on beat 1
note_f_sax = Note(74, 90, 6.0, 6.2)
sax.notes.append(note_f_sax)

# Bar 2: Bb on beat 3
note_bb_sax = Note(72, 90, 6.4, 6.6)
sax.notes.append(note_bb_sax)

# Bar 3: C on beat 2
note_c_sax = Note(76, 90, 7.2, 7.4)
sax.notes.append(note_c_sax)

# Bar 4: F on beat 1
note_f_sax = Note(74, 90, 8.0, 8.2)
sax.notes.append(note_f_sax)

# Add drum fills in Bar 3 and 4
for bar in [2, 3]:
    bar_start = bar * time_per_bar
    for i in range(8):
        time = bar_start + (i * time_per_beat / 2)
        note_hihat = Note(42, 80, time, time + 0.05)
        drums.notes.append(note_hihat)

# Save the MIDI file
pm.write('waynes_intro.mid')
