
import pretty_midi
import numpy as np

# Set tempo and time signature
tempo = 160  # BPM
time_signature = (4, 4)

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI()
pm.time_signature_changes = [pretty_midi.TimeSignature(*time_signature, 0.0)]
pm.tempos = [pretty_midi.TempoChange(tempo, 0.0)]

# Define instruments
# 1. Drums (Little Ray)
drums_program = pretty_midi.instrument_name_to_program("Acoustic Grand Piano")
drum_instrument = pretty_midi.Instrument(program=drums_program, is_drum=True)
pm.instruments.append(drum_instrument)

# 2. Bass (Marcus)
bass_program = pretty_midi.instrument_name_to_program("Double Bass")
bass_instrument = pretty_midi.Instrument(program=bass_program)
pm.instruments.append(bass_instrument)

# 3. Piano (Diane)
piano_program = pretty_midi.instrument_name_to_program("Acoustic Grand Piano")
piano_instrument = pretty_midi.Instrument(program=piano_program)
pm.instruments.append(piano_instrument)

# 4. Tenor Sax (You)
sax_program = pretty_midi.instrument_name_to_program("Soprano Sax")
sax_instrument = pretty_midi.Instrument(program=sax_program)
pm.instruments.append(sax_instrument)

# Define the time in seconds per bar
beats_per_bar = 4
beat_seconds = 60.0 / tempo
bar_seconds = beat_seconds * beats_per_bar

# Bar 1 (Little Ray – 3/4 of a bar)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    for beat in range(4):
        time = bar * bar_seconds + beat * beat_seconds
        # Hihat on every eighth
        for eighth in range(2):
            note = pretty_midi.Note(
                velocity=64,
                pitch=pretty_midi.note_number_to_name(57)[0],  # C4 (hihat)
                start=time + eighth * beat_seconds / 2,
                end=time + eighth * beat_seconds / 2 + 0.1
            )
            drum_instrument.notes.append(note)
        # Kick on 1 and 3
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(
                velocity=100,
                pitch=pretty_midi.note_number_to_name(36)[0],  # C1 (kick)
                start=time,
                end=time + 0.1
            )
            drum_instrument.notes.append(note)
        # Snare on 2 and 4
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(
                velocity=100,
                pitch=pretty_midi.note_number_to_name(44)[0],  # C2 (snare)
                start=time,
                end=time + 0.1
            )
            drum_instrument.notes.append(note)

# Bar 2-4: Everyone in (3 bars total)
for bar in range(1, 4):
    time = bar * bar_seconds

    # Marcus (Bass) – walking line, chromatic approaches
    # Start on F (F4) – walk down to E, D, C, B, A, G, F, etc.
    # These are all chromatic and create movement
    bass_notes = [
        (53, 0.0),  # F4
        (51, 0.25), # E4
        (49, 0.5),  # D4
        (48, 0.75), # C4
        (47, 1.0),  # B4
        (46, 1.25), # A4
        (45, 1.5),  # G4
        (53, 1.75)  # F4
    ]
    for note, offset in bass_notes:
        note_obj = pretty_midi.Note(
            velocity=70,
            pitch=note,
            start=time + offset,
            end=time + offset + 0.25
        )
        bass_instrument.notes.append(note_obj)

    # Diane (Piano) – 7th chords, comp on 2 and 4
    # F7 chord: F, A, C, E (F7 is F, A, C, E flat?) Let's use F7 as F, A, C, E flat
    # Comp on beat 2 and 4
    for beat in range(4):
        time_beat = time + beat * beat_seconds
        if beat == 1 or beat == 3:
            # F7 chord: F, A, C, E flat
            for pitch in [53, 60, 57, 59]:
                note_obj = pretty_midi.Note(
                    velocity=80,
                    pitch=pitch,
                    start=time_beat,
                    end=time_beat + 0.25
                )
                piano_instrument.notes.append(note_obj)
                # Add a rest between chords (optional)
                if beat == 1:
                    # Rest in piano for a few beats, creating space
                    rest_start = time_beat + 0.25
                    rest_end = time_beat + 0.75
                    rest_note = pretty_midi.Note(
                        velocity=0,
                        pitch=0,
                        start=rest_start,
                        end=rest_end
                    )
                    piano_instrument.notes.append(rest_note)

    # You (Tenor Sax) – short motif, one phrase
    # Start with a short phrase: F, C#, F, G, E
    # F (60), C# (63), F (60), G (62), E (60)
    # Play over 1.5s – start at bar 2
    sax_notes = [
        (60, 0.0),  # F (60)
        (63, 0.375), # C#
        (60, 0.75),  # F
        (62, 1.125), # G
        (59, 1.5)   # E
    ]
    for note, offset in sax_notes:
        note_obj = pretty_midi.Note(
            velocity=100,
            pitch=note,
            start=time + offset,
            end=time + offset + 0.25
        )
        sax_instrument.notes.append(note_obj)

# Save to a MIDI file
pm.write("jazz_intro_f_key.mid")
print("MIDI file saved as 'jazz_intro_f_key.mid'")
