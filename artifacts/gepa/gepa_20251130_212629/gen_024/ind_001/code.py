
import pretty_midi
import numpy as np

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set the key to D minor (key number 1 = C major, so D minor is key number 2)
pm.key_signature.key = 2  # D minor

# Define the time signature as 4/4
pm.time_signature.time_signature_numerator = 4
pm.time_signature.time_signature_denominator = 4

# Create instruments
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
piano_program = pretty_midi.instrument_name_to_program('Acoustic Piano')
drums_program = pretty_midi.instrument_name_to_program('Drum Kit')
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')

bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
drums = pretty_midi.Instrument(program=drums_program)
sax = pretty_midi.Instrument(program=sax_program)

pm.instruments = [bass, piano, drums, sax]

# Define time in seconds for a single beat at 160 BPM
bpm = 160
beats_per_bar = 4
seconds_per_beat = 60 / bpm
bar_length = beats_per_bar * seconds_per_beat  # 6.0 seconds for 4 bars

# Define note durations and rests (in seconds)
quarter = seconds_per_beat
eighth = quarter / 2
sixteenth = quarter / 4

#-------------------
# DRUMS (Little Ray)
#-------------------
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = {
    'kick': 36,  # MIDI note for kick
    'snare': 38,  # MIDI note for snare
    'hihat': 42   # MIDI note for hihat
}

for bar in range(4):
    for beat in range(4):
        time = bar * bar_length + beat * quarter
        if beat == 0 or beat == 2:
            # Kick on 1 and 3
            note = pretty_midi.Note(velocity=100, pitch=drum_notes['kick'], start=time, end=time + sixteenth)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            # Snare on 2 and 4
            note = pretty_midi.Note(velocity=100, pitch=drum_notes['snare'], start=time, end=time + sixteenth)
            drums.notes.append(note)
        # Hihat on every eighth
        note = pretty_midi.Note(velocity=80, pitch=drum_notes['hihat'], start=time, end=time + sixteenth)
        drums.notes.append(note)

#-------------------
# BASS (Marcus)
#-------------------
# Walking line, chromatic approaches
# Start on D (MIDI 62)
bass_notes = [62, 63, 64, 62, 60, 62, 63, 64]
for i, note in enumerate(bass_notes):
    time = i * quarter
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + quarter)
    bass.notes.append(note_obj)

#-------------------
# PIANO (Diane)
#-------------------
# 7th chords on 2 and 4
# Dm7: D, F, A, C
# G7: G, B, D, F
# Bm7: B, D, F#, A
# F7: F, A, C, E
# Chords on the 2nd and 4th beats

chord_notes = {
    0: [],  # Bar 0, beat 0: rest
    1: [62, 65, 67, 60],  # Dm7 on beat 2
    2: [],  # Bar 0, beat 2: rest
    3: [71, 74, 76, 72],  # G7 on beat 4
    4: [],  # Bar 1, beat 0: rest
    5: [67, 71, 73, 77],  # Bm7 on beat 2
    6: [],  # Bar 1, beat 2: rest
    7: [65, 69, 72, 76],  # F7 on beat 4
    8: [],  # Bar 2, beat 0: rest
    9: [67, 71, 73, 77],  # Bm7 on beat 2
    10: [],  # Bar 2, beat 2: rest
    11: [62, 65, 67, 60],  # Dm7 on beat 4
    12: [],  # Bar 3, beat 0: rest
    13: [62, 65, 67, 60]   # Dm7 on beat 2
}

for i, notes in enumerate(chord_notes):
    if notes:
        time = i * quarter
        for note in notes:
            note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + quarter)
            piano.notes.append(note_obj)

#-------------------
# SAX (You)
#-------------------
# One short motif — start it, leave it hanging. Make it sing.
# D (62), F (65), A (67), C (60), then rest
# Then return with a variation, but leave it unresolved.

# First motif (bar 0)
note1 = pretty_midi.Note(velocity=110, pitch=62, start=0, end=0.75)  # D, quarter note
note2 = pretty_midi.Note(velocity=110, pitch=65, start=0.75, end=1.25)  # F, eighth note
note3 = pretty_midi.Note(velocity=110, pitch=67, start=1.25, end=1.75)  # A, eighth note
note4 = pretty_midi.Note(velocity=110, pitch=60, start=1.75, end=2.5)  # C, quarter note

# Second motif (bar 2)
note5 = pretty_midi.Note(velocity=110, pitch=62, start=2.5, end=3.25)  # D, quarter note
note6 = pretty_midi.Note(velocity=110, pitch=65, start=3.25, end=3.75)  # F, eighth note
note7 = pretty_midi.Note(velocity=110, pitch=67, start=3.75, end=4.25)  # A, eighth note
note8 = pretty_midi.Note(velocity=110, pitch=60, start=4.25, end=4.5)  # C, half note — but leave it hanging

sax.notes.extend([note1, note2, note3, note4, note5, note6, note7, note8])

# Save the MIDI
pm.write('jazz_intro_d_minor.mid')
