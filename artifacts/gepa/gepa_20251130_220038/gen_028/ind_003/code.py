
import pretty_midi
import numpy as np

# Set up the MIDI file
midi = pretty_midi.PrettyMIDI()
midi.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]
midi.tempo_changes = [pretty_midi.TempoChange(160, 0)]
instrument_programs = {
    'drums': pretty_midi.instrument_name_to_program('Acoustic Grand Piano'),
    'bass': pretty_midi.instrument_name_to_program('Double Bass'),
    'piano': pretty_midi.instrument_name_to_program('Electric Piano 1'),
    'sax': pretty_midi.instrument_name_to_program('Soprano Sax')
}

# Create instruments
drum_program = pretty_midi.Instrument(program=instrument_programs['drums'])
bass_program = pretty_midi.Instrument(program=instrument_programs['bass'])
piano_program = pretty_midi.Instrument(program=instrument_programs['piano'])
sax_program = pretty_midi.Instrument(program=instrument_programs['sax'])

# Add instruments to MIDI file
midi.instruments = [drum_program, bass_program, piano_program, sax_program]

# Note: For drums, we use note numbers from the General MIDI standard
# Kick: 36, Snare: 38, Hi-Hat: 42, etc.

# Bar 1: Little Ray (drums) - Build tension
bar_length = 1.5  # 4/4 bar at 160 BPM is 1.5 seconds
bar1_start = 0.0

# Kick on 1 and 3, snare on 2 and 4, hi-hat on every eighth
for beat in range(4):
    time = bar1_start + beat * 0.375  # 0.375s per beat
    if beat % 2 == 0:  # Kick on 1 and 3
        drum_program.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1))
    else:  # Snare on 2 and 4
        drum_program.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=time, end=time + 0.1))
    
    # Hi-hat on every eighth
    drum_program.notes.append(pretty_midi.Note(velocity=60, pitch=42, start=time, end=time + 0.1))

# Bar 2: Marcus (bass) - Walking line, chromatic approaches
bar2_start = bar1_start + bar_length
# D minor: D, Eb, F, G, Ab, Bb, C
# Chromatic approach to D in bar 2
# Walking bass: D, Eb, F, G, Ab, Bb, C, D, Eb, F, G, Ab, Bb, C
# Key is D minor, but we're tonally open in the intro

bass_notes = [
    (bar2_start + 0.0, 62),  # D3
    (bar2_start + 0.375, 60),  # Eb3 (chromatic)
    (bar2_start + 0.75, 64),  # F3
    (bar2_start + 1.125, 67),  # G3
    (bar2_start + 1.5, 65),  # Ab3 (chromatic)
    (bar2_start + 1.875, 62),  # Bb3
    (bar2_start + 2.25, 67),  # C4
    (bar2_start + 2.625, 62),  # D3
    (bar2_start + 2.625 + 0.375, 60),  # Eb3
    (bar2_start + 2.625 + 0.75, 64),  # F3
    (bar2_start + 2.625 + 1.125, 67),  # G3
    (bar2_start + 2.625 + 1.5, 65),  # Ab3
    (bar2_start + 2.625 + 1.875, 62),  # Bb3
    (bar2_start + 2.625 + 2.25, 67),  # C4
    (bar2_start + 2.625 + 2.625, 64)  # D4 (resolve)
]

for time, pitch in bass_notes:
    bass_program.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + 0.25))

# Bar 2: Diane (piano) - 7th chords, comp on 2 and 4
bar2_piano_start = bar2_start

# D minor 7th
Dm7 = [62, 65, 67, 69]  # D, F, G, Bb
# G7 (chromatic approach to C)
G7 = [67, 71, 72, 69]  # G, B, B#, D
# C7 (chromatic approach to D)
C7 = [67, 71, 74, 72]  # C, E, G, B

# Comp on 2 and 4
for chord, time in zip([Dm7, G7, C7, Dm7], [bar2_piano_start + 0.75, bar2_piano_start + 1.125, bar2_piano_start + 1.5, bar2_piano_start + 2.25]):
    for pitch in chord:
        piano_program.notes.append(pretty_midi.Note(velocity=85, pitch=pitch, start=time, end=time + 0.25))

# Bar 2: Diane (piano) - Rest on 1 and 3, dynamic variation
# Add a low, brooding right-hand line (D minor melody with chromatic color)
melody_notes = [
    (bar2_piano_start, 62),  # D3
    (bar2_piano_start + 0.75, 60),  # Eb3
    (bar2_piano_start + 1.5, 64),  # F3
    (bar2_piano_start + 2.25, 67),  # G3
]

for time, pitch in melody_notes:
    piano_program.notes.append(pretty_midi.Note(velocity=60, pitch=pitch, start=time, end=time + 0.25))

# Bar 3-4: You (sax) - Melodic statement, concise and emotional
# D minor motif: D - Eb - F - G
# Voice leading with space, silence, and dynamic tension

sax_notes = [
    (bar2_start + bar_length + 0.0, 74),  # D4
    (bar2_start + bar_length + 0.375, 72),  # Eb4
    (bar2_start + bar_length + 0.75, 76),  # F4
    (bar2_start + bar_length + 1.125, 78),  # G4
    (bar2_start + bar_length + 1.5, 0),    # Rest (space)
    (bar2_start + bar_length + 1.875, 74),  # D4 (return)
    (bar2_start + bar_length + 2.25, 78),  # G4
    (bar2_start + bar_length + 2.625, 76),  # F4
    (bar2_start + bar_length + 2.625 + 0.375, 0),  # Rest
]

for time, pitch in sax_notes:
    if pitch != 0:
        sax_program.notes.append(pretty_midi.Note(velocity=105, pitch=pitch, start=time, end=time + 0.25))
    else:
        # Rest is implied by silence in the MIDI, but you can use a note with 0 velocity
        pass

# Save the MIDI file
midi.save('dante_intro.mid')
print("MIDI file 'dante_intro.mid' has been created.")
