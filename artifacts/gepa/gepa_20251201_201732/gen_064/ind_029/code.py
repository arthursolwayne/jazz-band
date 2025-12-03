
import pretty_midi
import numpy as np

# Set up the MIDI file
pm = pretty_midi.PrettyMIDI()
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]
pm.tempo_changes = [pretty_midi.TempoChange(160, 0)]
instrument_programs = {
    'drums': pretty_midi.instrument_name_to_program('Acoustic Grand Piano'),
    'bass': pretty_midi.instrument_name_to_program('Double Bass'),
    'piano': pretty_midi.instrument_name_to_program('Acoustic Grand Piano'),
    'sax': pretty_midi.instrument_name_to_program('Tenor Saxophone'),
}

# Create instruments
drums = pretty_midi.Instrument(program=instrument_programs['drums'], is_drum=True)
bass = pretty_midi.Instrument(program=instrument_programs['bass'])
piano = pretty_midi.Instrument(program=instrument_programs['piano'])
sax = pretty_midi.Instrument(program=instrument_programs['sax'])

pm.instruments = [drums, bass, piano, sax]

# Time per bar (seconds) = 60 / 160 * 4 = 1.5s
time_per_bar = 1.5
beat_time = time_per_bar / 4  # 0.375s

# Define F major scale: F, G, A, Bb, B, C, D
F_major_notes = [78, 80, 82, 83, 84, 87, 89]  # MIDI notes

# Bar 1 - Drums only
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i in range(4):
    time = i * beat_time
    if i % 2 == 0:
        # Kick on beat 1 and 3
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=36, start=time, end=time + 0.1))
    else:
        # Snare on 2 and 4
        drums.notes.append(pretty_midi.Note(velocity=95, pitch=38, start=time, end=time + 0.1))
    # Hihat on every eighth note
    hihat_time = time + 0.1875
    drums.notes.append(pretty_midi.Note(velocity=60, pitch=42, start=hihat_time, end=hihat_time + 0.05))

# Bar 2: Everyone in
# Key: F major
# Chord progression: Fmaj7 -> Bb7 -> Cm7 -> D7

# Bass line: F, Bb, C, D
bass_notes = [78, 83, 87, 89]
for i, note in enumerate(bass_notes):
    start = i * beat_time
    end = start + beat_time
    bass.notes.append(pretty_midi.Note(velocity=70, pitch=note, start=start, end=end))

# Piano chords: Fmaj7, Bb7, Cm7, D7
chords = [
    [78, 82, 87, 90],  # Fmaj7
    [83, 87, 91, 93],  # Bb7
    [87, 90, 94, 97],  # Cm7
    [89, 93, 97, 101], # D7
]

# Diane plays on beats 2 and 4
for i, chord in enumerate(chords):
    if i in [1, 3]:
        start = i * beat_time
        end = start + beat_time
        for pitch in chord:
            piano.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=end))

# Saxophone motif: Start on F, move to Bb, then back to F, leave hanging a bit
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=78, start=0, end=0.5),  # F
    pretty_midi.Note(velocity=100, pitch=83, start=0.5, end=1.0), # Bb
    pretty_midi.Note(velocity=100, pitch=78, start=1.0, end=1.5), # F
]

for note in sax_notes:
    sax.notes.append(note)

# Save the MIDI file
pm.write('jazz_intro.mid')
print("MIDI file saved as jazz_intro.mid")
