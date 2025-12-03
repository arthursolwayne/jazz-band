
import pretty_midi
import numpy as np

# Create a PrettyMIDI object with the tempo set to 160 BPM (which is 160 beats per minute)
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instruments
bass_program = pretty_midi.instrument_name_to_program('Acoustic Bass')
piano_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
drums_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')  # Drums use the same program
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')

# Add instruments
bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
drums = pretty_midi.Instrument(program=drums_program)
sax = pretty_midi.Instrument(program=sax_program)

pm.instruments.append(bass)
pm.instruments.append(piano)
pm.instruments.append(drums)
pm.instruments.append(sax)

# Define time in seconds (160 BPM = 0.375s per beat, 6 seconds for 4 bars)
time = 0.0

# --- Bar 1: Little Ray on drums (driving rhythm with space)
# Kick on 1 and 3
drum_kick = pretty_midi.Note(
    velocity=90,
    pitch=36,  # Kick drum
    start=time,
    end=time + 0.375
)
drums.notes.append(drum_kick)

drum_kick = pretty_midi.Note(
    velocity=90,
    pitch=36,
    start=time + 0.75,
    end=time + 1.125
)
drums.notes.append(drum_kick)

# Snare on 2 and 4
drum_snare = pretty_midi.Note(
    velocity=95,
    pitch=38,  # Snare drum
    start=time + 0.375,
    end=time + 0.75
)
drums.notes.append(drum_snare)

drum_snare = pretty_midi.Note(
    velocity=95,
    pitch=38,
    start=time + 1.125,
    end=time + 1.5
)
drums.notes.append(drum_snare)

# Hi-hat on every eighth
hihat_pitches = [42, 46]  # Closed and open hi-hats
for i in range(0, 8):
    pitch = hihat_pitches[i % 2]
    note_start = time + i * 0.1875
    note_end = note_start + 0.1875
    hihat = pretty_midi.Note(
        velocity=80,
        pitch=pitch,
        start=note_start,
        end=note_end
    )
    drums.notes.append(hihat)

time += 1.5  # Move to bar 2

# --- Bar 2: All instruments enter
# Bass (Marcus) - walking line in F minor: F - G - Ab - A - Bb - B - C - D
# Notes in MIDI: F = 65, G = 67, Ab = 68, A = 69, Bb = 70, B = 71, C = 72, D = 74
# Roots and fifths with chromatic approaches, keeping it grounded and expressive

bass_notes = [65, 67, 68, 69, 70, 71, 72, 74]
for note in bass_notes:
    bass_note = pretty_midi.Note(
        velocity=80,
        pitch=note,
        start=time,
        end=time + 0.375
    )
    bass.notes.append(bass_note)
    time += 0.375

# Piano (Diane) - open voicings, resolve on the last bar
# Bar 2: Fm7 (F, A, C, D)
midi_notes = [65, 74, 77, 79]
for note in midi_notes:
    piano_note = pretty_midi.Note(
        velocity=100,
        pitch=note,
        start=time - 0.375,
        end=time
    )
    piano.notes.append(piano_note)

# Bar 3: Cm7 (C, Eb, G, Bb)
midi_notes = [72, 69, 77, 70]
for note in midi_notes:
    piano_note = pretty_midi.Note(
        velocity=100,
        pitch=note,
        start=time,
        end=time + 0.375
    )
    piano.notes.append(piano_note)

# Bar 4: G7 (G, B, D, F)
midi_notes = [67, 71, 74, 65]
for note in midi_notes:
    piano_note = pretty_midi.Note(
        velocity=100,
        pitch=note,
        start=time + 0.75,
        end=time + 1.125
    )
    piano.notes.append(piano_note)

time = 1.5  # Reset time to bar 2 start for sax

# --- Sax (Dante) - one short motif that sings, whispers, and lingers
# F, Bb, C, Ab (Motif: F → Bb → C → Ab)
sax_notes = [65, 70, 72, 68]
for i, note in enumerate(sax_notes):
    start = time + i * 0.5
    end = start + 0.5 if i < len(sax_notes) - 1 else start + 0.3  # last note lingers
    sax_note = pretty_midi.Note(
        velocity=105,
        pitch=note,
        start=start,
        end=end
    )
    sax.notes.append(sax_note)

# Save the MIDI file
pm.write('jazz_intro_wayne.midi')
print("MIDI file 'jazz_intro_wayne.midi' created.")
