
import pretty_midi
import numpy as np

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create a time signature (4/4)
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Set the key to D minor (key number 1)
pm.key_signature_changes = [pretty_midi.KeySignature(1, 0)]

# Create instruments
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
piano_program = pretty_midi.instrument_name_to_program('Acoustic Piano')
drums_program = pretty_midi.instrument_name_to_program('Drums')
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')

bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
drums = pretty_midi.Instrument(program=drums_program)
sax = pretty_midi.Instrument(program=sax_program)

pm.instruments = [bass, piano, drums, sax]

# Set tempo
pm.tempo_changes = [pretty_midi.TempoChange(160, 0)]

# Time per bar in seconds (BPM = 160, 4/4 time)
time_per_bar = 60 / 160 * 4  # 1.5 seconds per bar
time_per_beat = 60 / 160  # 0.375 seconds per beat

# Bar 1: Drums only
# Kick on 1 and 3, snare on 2 and 4
for bar in range(1):
    for beat in range(4):
        time = bar * time_per_bar + beat * time_per_beat
        if beat == 0 or beat == 2:
            # Kick (note 36 is kick drum)
            note = pretty_midi.Note(velocity=90, pitch=36, start=time, end=time + 0.1)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            # Snare (note 38 is snare)
            note = pretty_midi.Note(velocity=95, pitch=38, start=time, end=time + 0.1)
            drums.notes.append(note)
        # Hi-hat on every eighth note
        for eighth in range(2):
            note_time = time + (eighth * 0.1875)
            note = pretty_midi.Note(velocity=80, pitch=42, start=note_time, end=note_time + 0.05)
            drums.notes.append(note)

# Bar 2-4: Full ensemble
for bar in range(1, 4):
    bar_start = bar * time_per_bar

    # Bass line: Walking line with chromatic passing tones
    # Bass notes (Dm7 chord: D, F, A, C)
    # Walking bass line: D -> Eb (chromatic) -> F -> Gb (chromatic) -> G -> A -> Bb -> B -> C
    bass_notes = [62, 63, 65, 66, 67, 69, 70, 71, 72]
    for i, note in enumerate(bass_notes):
        start = bar_start + (i * 0.375)
        end = start + 0.375
        note_obj = pretty_midi.Note(velocity=75, pitch=note, start=start, end=end)
        bass.notes.append(note_obj)

    # Piano: 7th chords, comp on 2 and 4
    # Dm7: D, F, A, C
    # Time on beat 2 and 4 (0.75 and 1.5 seconds into bar)
    for beat in [1, 3]:
        time = bar_start + beat * time_per_beat
        # Root position Dm7
        chord_notes = [62, 65, 67, 72]
        for note in chord_notes:
            note_obj = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25)
            piano.notes.append(note_obj)

    # Drums: Continue with same pattern
    for beat in range(4):
        time = bar_start + beat * time_per_beat
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=90, pitch=36, start=time, end=time + 0.1)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=95, pitch=38, start=time, end=time + 0.1)
            drums.notes.append(note)
        for eighth in range(2):
            note_time = time + (eighth * 0.1875)
            note = pretty_midi.Note(velocity=80, pitch=42, start=note_time, end=note_time + 0.05)
            drums.notes.append(note)

    # Sax: Motif — short phrase that ends on a question
    if bar == 1:
        # Bar 2: Start the motif
        # D (62), F (65), G (67), rest
        # D -> F -> G -> rest
        sax_notes = [62, 65, 67]
        for i, note in enumerate(sax_notes):
            start = bar_start + (i * 0.375)
            end = start + 0.375
            note_obj = pretty_midi.Note(velocity=100, pitch=note, start=start, end=end)
            sax.notes.append(note_obj)
        # End on a rest (no note on last eighth)
    elif bar == 2:
        # Bar 3: Continue the motif
        # C (60), D (62), rest, rest
        sax_notes = [60, 62]
        for i, note in enumerate(sax_notes):
            start = bar_start + (i * 0.375)
            end = start + 0.375
            note_obj = pretty_midi.Note(velocity=100, pitch=note, start=start, end=end)
            sax.notes.append(note_obj)
        # End on rest
    elif bar == 3:
        # Bar 4: Resolve with a question ending
        # Bb (62?), F (65), rest, rest
        # Note: Dm scale: D, Eb, F, G, A, Bb, C
        sax_notes = [64, 65]
        for i, note in enumerate(sax_notes):
            start = bar_start + (i * 0.375)
            end = start + 0.375
            note_obj = pretty_midi.Note(velocity=100, pitch=note, start=start, end=end)
            sax.notes.append(note_obj)
        # End with a rest — question mark

# Save the MIDI file
pm.write("dante_intro.mid")

print("MIDI file 'dante_intro.mid' has been created.")
