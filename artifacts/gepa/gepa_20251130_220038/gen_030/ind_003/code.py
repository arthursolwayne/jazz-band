
import pretty_midi
import numpy as np

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Time signature: 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Key signature: D minor
pm.key_signature_changes = [pretty_midi.KeySignature(2, 0)]

# Create instruments
drum_program = pretty_midi.instrument_name_to_program("Acoustic Drums")
bass_program = pretty_midi.instrument_name_to_program("Fretless Bass")
piano_program = pretty_midi.instrument_name_to_program("Electric Piano 1")
sax_program = pretty_midi.instrument_name_to_program("Tenor Saxophone")

drum_inst = pretty_midi.Instrument(program=drum_program)
bass_inst = pretty_midi.Instrument(program=bass_program)
piano_inst = pretty_midi.Instrument(program=piano_program)
sax_inst = pretty_midi.Instrument(program=sax_program)

# Add instruments to the MIDI file
pm.instruments = [drum_inst, bass_inst, piano_inst, sax_inst]

# Time per beat (in seconds) = 60 / BPM
time_per_beat = 60 / 160
time_per_bar = 4 * time_per_beat  # 1.5 seconds per bar
time_per_eighth = time_per_beat / 2

# Bar 1: Drums (tension)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for beat in range(4):
    time = beat * time_per_beat
    # Kick on beat 1 and 3
    if beat in [0, 2]:
        drum_inst.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1))
    # Snare on beat 2 and 4
    if beat in [1, 3]:
        drum_inst.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.1))
    # Hi-hat on every eighth
    for eighth in range(2):
        hihat_time = time + eighth * time_per_eighth
        drum_inst.notes.append(pretty_midi.Note(velocity=60, pitch=42, start=hihat_time, end=hihat_time + 0.05))

# Bar 2-4: Full ensemble

# Bass line (walking line in Dm)
bass_notes = [
    (0, 50, 36),  # D (root)
    (time_per_beat, 70, 40),  # F (3rd)
    (2 * time_per_beat, 70, 43),  # A♭ (5th)
    (3 * time_per_beat, 70, 44),  # B♭ (7th)
    (4 * time_per_beat, 50, 36),  # D
    (5 * time_per_beat, 70, 40),
    (6 * time_per_beat, 70, 43),
    (7 * time_per_beat, 70, 44),
    (8 * time_per_beat, 50, 36),
    (9 * time_per_beat, 70, 40),
    (10 * time_per_beat, 70, 43),
    (11 * time_per_beat, 70, 44),
    (12 * time_per_beat, 50, 36)
]
for note in bass_notes:
    start, velocity, pitch = note
    bass_inst.notes.append(pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + 0.25))

# Piano chords (7th chords, comp on 2 and 4)
# Dm7♭5: D, F, A♭, C
# Dm7♭13: D, F, A♭, B♭, C
piano_notes = [
    (time_per_beat, 80, 62),  # F
    (time_per_beat, 80, 64),  # A♭
    (time_per_beat, 80, 60),  # D
    (time_per_beat, 80, 67),  # C

    (2 * time_per_beat, 80, 62),  # F
    (2 * time_per_beat, 80, 64),  # A♭
    (2 * time_per_beat, 80, 60),  # D
    (2 * time_per_beat, 80, 67),  # C

    (3 * time_per_beat, 80, 62),  # F
    (3 * time_per_beat, 80, 64),  # A♭
    (3 * time_per_beat, 80, 60),  # D
    (3 * time_per_beat, 80, 67),  # C
]

for note in piano_notes:
    start, velocity, pitch = note
    piano_inst.notes.append(pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + 0.25))

# Tenor Sax: A short, emotional motif (2 notes)
# Dm7 scale: D, E♭, F, G, A♭, B♭, C
# Motif: D (62) -> F (65), long sustain on F
sax_notes = [
    (0, 90, 62),   # D
    (0.3, 90, 65), # F
    (0.3, 90, 65), # F (sustained)
    (1.0, 0, 65)   # End of sustain
]
for note in sax_notes:
    start, velocity, pitch = note
    sax_inst.notes.append(pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + 0.2 if velocity != 0 else start))

# Write to MIDI file
pm.write("the_whisper_before_the_storm.mid")
print("MIDI file saved as 'the_whisper_before_the_storm.mid'")
