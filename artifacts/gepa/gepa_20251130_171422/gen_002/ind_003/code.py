
import pretty_midi
import numpy as np

# Set up the MIDI file
pm = pretty_midi.PrettyMidi(initial_tempo=160)  # 160 BPM
instrument_programs = {
    'tenor_sax': pretty_midi.instrument_name_to_program('Tenor Saxophone'),
    'bass': pretty_midi.instrument_name_to_program('Acoustic Bass'),
    'piano': pretty_midi.instrument_name_to_program('Acoustic Grand Piano'),
    'drums': pretty_midi.instrument_name_to_program('Acoustic Grand Piano')  # Drum tracks use the same program
}

# Create instruments
tenor_sax = pretty_midi.Instrument(program=instrument_programs['tenor_sax'])
bass = pretty_midi.Instrument(program=instrument_programs['bass'])
piano = pretty_midi.Instrument(program=instrument_programs['piano'])
drums = pretty_midi.Instrument(program=instrument_programs['drums'], is_drum=True)

# Add instruments to the MIDI file
pm.instruments.append(tenor_sax)
pm.instruments.append(bass)
pm.instruments.append(piano)
pm.instruments.append(drums)

# Time settings in seconds
bar_length = 1.5  # 6 seconds for 4 bars
beat_length = 0.375  # 160 BPM = 0.375 seconds per beat
note_length = 0.1875  # Half a beat (approx 1/8 note)

# Drum pattern: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
def create_drums():
    for bar in range(4):
        for beat in range(4):
            time = bar * bar_length + beat * beat_length
            # Hi-hat on every eighth
            for eighth in range(2):
                midi_time = time + eighth * beat_length / 2
                hi_hat = pretty_midi.Note(velocity=60, pitch=42, start=midi_time, end=midi_time + note_length / 2)
                drums.notes.append(hi_hat)
            # Kick on 1 and 3
            if beat == 0 or beat == 2:
                kick = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + note_length)
                drums.notes.append(kick)
            # Snare on 2 and 4
            if beat == 1 or beat == 3:
                snare = pretty_midi.Note(velocity=90, pitch=38, start=time, end=time + note_length)
                drums.notes.append(snare)

# Bass line: Walking line, chromatic approaches, never the same note twice
def create_bass():
    # F7 chord: F, A, C, E, G, Bb, Db
    # Bass line in F major, chromatic movement
    bass_notes = [77, 79, 80, 78, 79, 81, 82, 80, 79, 77, 78, 80, 82, 81, 80, 79]  # F, A, C, Bb, A, B, C#, B, A, F, G, C, D, C, B, A
    for i, note in enumerate(bass_notes):
        time = i * beat_length
        duration = beat_length
        bass_note = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + duration)
        bass.notes.append(bass_note)

# Piano: 7th chords, comp on 2 and 4
def create_piano():
    # 7th chords: F7, Bb7, E7, A7 (for 4 bars)
    # Chords on beats 2 and 4
    chords = [
        (77, 79, 81, 82),  # F7
        (74, 76, 78, 80),  # Bb7
        (79, 81, 83, 85),  # E7
        (77, 79, 82, 84)   # A7
    ]
    for bar in range(4):
        for beat in range(2, 5, 2):  # 2 and 4
            time = bar * bar_length + beat * beat_length
            for pitch in chords[bar]:
                piano_note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + note_length)
                piano.notes.append(piano_note)

# Tenor sax: Motif, concise, with a clear beginning and implied ending
def create_tenor_sax():
    # Motif: F - Bb - C - F (rest), then return with variation
    # This motif starts on 1, leaves a rest on 3, and resolves on 4
    motif = [77, 74, 80, 77, 79, 82, 74, 77]  # F, Bb, C, F (rest), B, D, Bb, F
    for i, note in enumerate(motif):
        time = (i // 2) * bar_length + (i % 2) * beat_length
        duration = beat_length
        if i % 2 == 1:
            time = time + beat_length / 2  # Offset for the second note in each pair
        tenor_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + duration)
        tenor_sax.notes.append(tenor_note)

# Create the parts
create_drums()
create_bass()
create_piano()
create_tenor_sax()

# Save the MIDI file
pm.write("four_bar_intro.mid")
print("MIDI file 'four_bar_intro.mid' has been created.")
