
import pretty_midi
import numpy as np

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Time signature: 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]

# Key: F minor (Fm)
pm.key_signature_changes = [pretty_midi.KeySignature(5, 0.0)]  # F minor is key number 5

# Create instruments
drums_program = pretty_midi.programs[pretty_midi.INSTRUMENT_DRUMS]
bass_program = pretty_midi.programs[pretty_midi.INSTRUMENT_BASS]
piano_program = pretty_midi.programs[pretty_midi.INSTRUMENT_PIANO]
sax_program = pretty_midi.programs[pretty_midi.INSTRUMENT_SAXOPHONE]

# Create instrument tracks
drum_track = pretty_midi.Instrument(program=drums_program)
bass_track = pretty_midi.Instrument(program=bass_program)
piano_track = pretty_midi.Instrument(program=piano_program)
sax_track = pretty_midi.Instrument(program=sax_program)

pm.instruments = [drum_track, bass_track, piano_track, sax_track]

# Time per bar at 160 BPM (seconds)
time_per_bar = 60.0 / 160 * 4
time_per_beat = time_per_bar / 4

# BAR 1: Little Ray on drums
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    for beat in range(4):
        time = bar * time_per_bar + beat * time_per_beat
        # Kick on 1 and 3
        if beat in [0, 2]:
            drum_track.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1))
        # Snare on 2 and 4
        if beat in [1, 3]:
            drum_track.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.1))
        # Hi-hats on every eighth (0.125 beat)
        for eighth in range(2):
            drum_track.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time + eighth * 0.125, end=time + eighth * 0.125 + 0.05))

# BAR 2-4: Full ensemble
# Time starts at bar 1 (time = time_per_bar)
start_time = time_per_bar

# Bass line: Walking line, chromatic approaches, no repeated notes
bass_notes = [36, 37, 35, 34, 36, 37, 35, 33, 35, 36, 34, 33]  # Fm7 walking line
for i, note in enumerate(bass_notes):
    time = start_time + i * time_per_beat
    bass_track.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords, comp on 2 and 4
# Fm7 = F, Ab, C, Eb
# Bbm7 = Bb, Db, F, Ab
# Dm7 = D, F, A, C
# Gm7 = G, Bb, D, F

# Bar 2: Fm7 on beat 2 and 4
for beat in [1, 3]:
    time = start_time + beat * time_per_beat
    for pitch in [53, 50, 57, 55]:  # F, Ab, C, Eb
        piano_track.notes.append(pretty_midi.Note(velocity=85, pitch=pitch, start=time, end=time + 0.1))

# Bar 3: Bbm7 on beat 2 and 4
for beat in [1, 3]:
    time = start_time + (beat + 4) * time_per_beat
    for pitch in [58, 55, 53, 50]:  # Bb, Db, F, Ab
        piano_track.notes.append(pretty_midi.Note(velocity=85, pitch=pitch, start=time, end=time + 0.1))

# Bar 4: Dm7 on beat 2 and 4
for beat in [1, 3]:
    time = start_time + (beat + 8) * time_per_beat
    for pitch in [58, 53, 62, 57]:  # D, F, A, C
        piano_track.notes.append(pretty_midi.Note(velocity=85, pitch=pitch, start=time, end=time + 0.1))

# Saxophone: One short motif, searching, not scale runs
# Motif: F, Ab, Bb, D
# Start on bar 2, beat 1
sax_notes = [53, 50, 58, 62]
for i, note in enumerate(sax_notes):
    time = start_time + (i + 1) * time_per_beat
    sax_track.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# End the piece at the end of bar 4
pm.end_time = start_time + 3 * time_per_bar

# Save the MIDI file
pm.write("dante_intro.mid")
print("MIDI file written as 'dante_intro.mid'")
