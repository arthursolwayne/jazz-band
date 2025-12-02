
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i in range(4):
    kick_time = i * 1.5 + 0.0
    snare_time = i * 1.5 + 0.75
    for j in range(2):
        hihat_time = i * 1.5 + j * 0.375
        note = pretty_midi.Note(velocity=100, pitch=42, start=hihat_time, end=hihat_time + 0.125)
        drums.notes.append(note)
    note = pretty_midi.Note(velocity=110, pitch=36, start=kick_time, end=kick_time + 0.125)
    drums.notes.append(note)
    note = pretty_midi.Note(velocity=110, pitch=38, start=snare_time, end=snare_time + 0.125)
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus - walking line, chromatic approaches
bass_notes = [
    (1.5, 46, 100), # F
    (1.875, 47, 100), # Gb
    (2.25, 45, 100), # E
    (2.625, 48, 100), # Ab
    (2.875, 47, 100), # Gb
    (3.25, 46, 100), # F
    (3.625, 44, 100), # D
    (4.0, 46, 100), # F
    (4.375, 47, 100), # Gb
    (4.75, 45, 100), # E
    (5.125, 48, 100), # Ab
    (5.5, 47, 100), # Gb
    (5.875, 46, 100), # F
]
for time, pitch, vel in bass_notes:
    note = pretty_midi.Note(velocity=vel, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: Diane - 7th chords, comp on 2 and 4
chords = [
    (1.5, [12, 16, 19, 21], 80), # F7
    (2.25, [12, 16, 19, 21], 80), # F7
    (3.0, [12, 16, 19, 21], 80), # F7
    (3.75, [12, 16, 19, 21], 80), # F7
    (4.5, [12, 16, 19, 21], 80), # F7
    (5.25, [12, 16, 19, 21], 80), # F7
]
for time, pitches, vel in chords:
    for pitch in pitches:
        note = pretty_midi.Note(velocity=vel, pitch=pitch, start=time, end=time + 0.25)
        piano.notes.append(note)

# Sax: Dante - motif starts at 1.5, ends at 3.0
# Motif: F (46), Gb (47), Ab (48), Gb (47)
sax_notes = [
    (1.5, 46, 110, 0.25),
    (1.75, 47, 110, 0.25),
    (2.0, 48, 110, 0.25),
    (2.25, 47, 110, 0.25),
    (3.0, 46, 110, 0.25),
]
for time, pitch, vel, dur in sax_notes:
    note = pretty_midi.Note(velocity=vel, pitch=pitch, start=time, end=time + dur)
    sax.notes.append(note)

# Drums: continue kick, snare, hihat for bars 2-4
for i in range(2, 4):
    kick_time = i * 1.5 + 0.0
    snare_time = i * 1.5 + 0.75
    for j in range(2):
        hihat_time = i * 1.5 + j * 0.375
        note = pretty_midi.Note(velocity=100, pitch=42, start=hihat_time, end=hihat_time + 0.125)
        drums.notes.append(note)
    note = pretty_midi.Note(velocity=110, pitch=36, start=kick_time, end=kick_time + 0.125)
    drums.notes.append(note)
    note = pretty_midi.Note(velocity=110, pitch=38, start=snare_time, end=snare_time + 0.125)
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
