
import pretty_midi
import numpy as np

# Create a PrettyMIDI object with 160 BPM (4/4 time)
pm = pretty_midi.PrettyMIDI(initial_tempo=160)
instrument = pretty_midi.Instrument(program=64)  # Tenor sax
pm.instruments.append(instrument)

# Time settings
BPM = 160
BAR_DURATION = 1.5  # seconds per bar
BEAT_DURATION = BAR_DURATION / 4  # 0.375s per beat
NOTE_DURATION = 0.25  # quarter note in seconds

# Key: F minor
Fm_notes = [53, 55, 57, 58, 60, 61, 63]  # F, Gb, Ab, Bb, B, C, D
Fm_intervals = [0, 1, 3, 5, 6, 7, 9]  # Fm scale

# Add notes to the instrument with timing and dynamics
# Bar 1: Little Ray alone - cymbal swells, tension, waiting
# (No sax notes here, but we can simulate with a percussion instrument)
# Let's add a 'hi-hat' effect on every eighth note, but not too aggressive
# We'll use a drum instrument for these

# Create a percussion instrument for cymbals and hihat
drum_instrument = pretty_midi.Instrument(program=11)  # percussion
pm.instruments.append(drum_instrument)

# Bar 1: Hihat on every eighth, kick on 1 and 3
# We'll place a "hi-hat" or "cymbal" sound on every eighth note
# and a kick on the downbeats (1 and 3)

for i in range(4):  # 4 beats in a bar
    # Hihat on every eighth note
    for j in range(2):  # 2 eighth notes per beat
        time = i * BEAT_DURATION + j * (BEAT_DURATION / 2)
        note = pretty_midi.Note(
            velocity=60,  # light hihat
            pitch=42,  # cymbal patch
            start=time,
            end=time + 0.05
        )
        drum_instrument.notes.append(note)

    # Kick on 1 and 3
    if i == 0 or i == 2:
        time = i * BEAT_DURATION
        note = pretty_midi.Note(
            velocity=90,  # strong kick
            pitch=35,  # kick drum
            start=time,
            end=time + 0.1
        )
        drum_instrument.notes.append(note)

# Bar 2-4: Full ensemble comes in

# Tenor sax part (you)
tenor_notes = [
    # Bar 2: Start the motif
    (53, 0.0, 0.5),  # F, on beat 1, 1/2 note (staccato)
    (58, 0.5, 0.25),  # Bb, on beat 2, 1/4 note
    (57, 1.0, 0.25),  # Ab, on beat 3
    (53, 1.5, 0.5),  # F, on beat 4, 1/2 note (rests in between)
    
    # Bar 3: Leave it hanging, just a rest (tension)
    (53, 1.5, 0.0),  # Rest
    (53, 2.0, 0.0),  # Rest
    (53, 2.5, 0.0),  # Rest
    (53, 3.0, 0.0),  # Rest
    
    # Bar 4: Return with a question — incomplete motif
    (58, 3.0, 0.25),  # Bb
    (57, 3.5, 0.25),  # Ab
    (53, 4.0, 0.0),  # Rest
    (53, 4.5, 0.25),  # F, at the end — hanging, unresolved
]

# Add tenor sax notes
for pitch, start, duration in tenor_notes:
    if duration > 0:
        note = pretty_midi.Note(
            velocity=100,
            pitch=pitch,
            start=start,
            end=start + duration
        )
        instrument.notes.append(note)

# Bass line (Marcus) - walking line, chromatic, no same note twice
# In Fm: F, Gb, Ab, Bb, B, C, D, Eb, F
# Walking line, 16th notes, chromatic passing
bass_notes = [
    # Bar 2
    (53, 0.0, 0.125),  # F
    (54, 0.125, 0.125),  # Gb (chromatic)
    (55, 0.25, 0.125),  # Ab
    (57, 0.375, 0.125),  # Bb
    (60, 0.5, 0.125),  # B
    (61, 0.625, 0.125),  # C
    (62, 0.75, 0.125),  # Db (chromatic)
    (63, 0.875, 0.125),  # D
    (64, 1.0, 0.125),  # Eb (chromatic)
    
    # Bar 3
    (63, 1.125, 0.125),  # D
    (62, 1.25, 0.125),  # Db
    (61, 1.375, 0.125),  # C
    (60, 1.5, 0.125),  # B
    (57, 1.625, 0.125),  # Bb
    (55, 1.75, 0.125),  # Ab
    (54, 1.875, 0.125),  # Gb
    (53, 2.0, 0.125),  # F
    
    # Bar 4
    (53, 2.125, 0.125),  # F
    (54, 2.25, 0.125),  # Gb
    (55, 2.375, 0.125),  # Ab
    (57, 2.5, 0.125),  # Bb
    (60, 2.625, 0.125),  # B
    (61, 2.75, 0.125),  # C
    (62, 2.875, 0.125),  # Db
    (63, 3.0, 0.125),  # D
    (64, 3.125, 0.125),  # Eb
    (63, 3.25, 0.125),  # D
    (62, 3.375, 0.125),  # Db
    (61, 3.5, 0.125),  # C
    (60, 3.625, 0.125),  # B
    (57, 3.75, 0.125),  # Bb
    (55, 3.875, 0.125),  # Ab
    (53, 4.0, 0.125)  # F
]

# Add bass notes
bass_instrument = pretty_midi.Instrument(program=33)  # Acoustic Bass
pm.instruments.append(bass_instrument)

for pitch, start, duration in bass_notes:
    note = pretty_midi.Note(
        velocity=70,
        pitch=pitch,
        start=start,
        end=start + duration
    )
    bass_instrument.notes.append(note)

# Piano (Diane) - 7th chords, comp on 2 and 4
piano_instrument = pretty_midi.Instrument(program=0)  # Acoustic Piano
pm.instruments.append(piano_instrument)

# Fm7 = F, Ab, Bb, Db
# Dm7 = D, F, Ab, Bb (if needed)
# Walk 7th chords on 2 and 4
piano_notes = [
    # Bar 2
    (53, 0.5, 0.125),  # F (on beat 2)
    (57, 0.5, 0.125),  # Ab
    (57, 0.5, 0.125),  # Bb
    (55, 0.5, 0.125),  # Db

    (53, 1.5, 0.125),  # F (on beat 4)
    (57, 1.5, 0.125),  # Ab
    (57, 1.5, 0.125),  # Bb
    (55, 1.5, 0.125),  # Db

    # Bar 3
    (53, 2.0, 0.125),  # F (on beat 2)
    (57, 2.0, 0.125),  # Ab
    (57, 2.0, 0.125),  # Bb
    (55, 2.0, 0.125),  # Db

    (53, 3.0, 0.125),  # F (on beat 4)
    (57, 3.0, 0.125),  # Ab
    (57, 3.0, 0.125),  # Bb
    (55, 3.0, 0.125),  # Db

    # Bar 4
    (53, 3.5, 0.125),  # F (on beat 2)
    (57, 3.5, 0.125),  # Ab
    (57, 3.5, 0.125),  # Bb
    (55, 3.5, 0.125),  # Db
]

for pitch, start, duration in piano_notes:
    note = pretty_midi.Note(
        velocity=90,
        pitch=pitch,
        start=start,
        end=start + duration
    )
    piano_instrument.notes.append(note)

# Drums (Little Ray) - kick on 1 and 3, snare on 2 and 4, hihat on every 8th
# We already added hihat earlier, but we can fill the rest
# Add snare and kick again for clarity

# Bar 2-4: Snare on 2 and 4, kick on 1 and 3
for i in range(2, 4):
    for j in range(4):
        time = i * BEAT_DURATION + j * BEAT_DURATION
        if j == 1 or j == 3:
            note = pretty_midi.Note(
                velocity=80,
                pitch=62,  # Snare
                start=time,
                end=time + 0.1
            )
            drum_instrument.notes.append(note)
        elif j == 0 or j == 2:
            note = pretty_midi.Note(
                velocity=90,
                pitch=35,  # Kick
                start=time,
                end=time + 0.1
            )
            drum_instrument.notes.append(note)

# Save the MIDI file
pm.write('dante_intro.mid')
