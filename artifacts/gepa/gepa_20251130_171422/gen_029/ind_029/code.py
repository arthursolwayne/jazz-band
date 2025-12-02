
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Build tension with sparse, dynamic variation
drum_notes = [
    (0.0, 38, 100),       # Snare on 2
    (0.375, 42, 60),      # Hihat on & of 1
    (0.75, 36, 90),       # Kick on 3
    (1.125, 42, 60),      # Hihat on & of 3
    (1.5, 38, 100)        # Snare on 4
]
for time, note, velocity in drum_notes:
    dr = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Saxophone motif (Fm7 -> Bb -> Ab -> G -> F)
# Concise, emotional, not scale-based
sax_notes = [
    (1.5, 64, 100, 0.375), # F (64)
    (1.75, 62, 100, 0.375), # Ab (62)
    (2.125, 60, 100, 0.375), # G (60)
    (2.5, 64, 100, 0.375), # F (64)
    (2.75, 71, 100, 0.375), # Bb (71)
    (3.125, 67, 100, 0.375), # Eb (67)
    (3.5, 64, 100, 0.375), # F (64)
    (3.875, 62, 100, 0.375), # Ab (62)
    (4.25, 60, 100, 0.375), # G (60)
    (4.625, 64, 100, 0.375), # F (64)
    (4.875, 67, 100, 0.375), # Eb (67)
    (5.25, 64, 100, 0.375), # F (64)
    (5.5, 71, 100, 0.375), # Bb (71)
    (5.875, 64, 100, 0.375) # F (64)
]
for time, pitch, velocity, duration in sax_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + duration)
    sax.notes.append(note)

# Bass line: melodic, active, chromatic approaches
bass_notes = [
    (1.5, 47, 90, 0.5),    # F (47)
    (1.75, 48, 90, 0.5),   # Gb (48)
    (2.25, 45, 90, 0.5),   # Eb (45)
    (2.75, 47, 90, 0.5),   # F (47)
    (3.0, 50, 90, 0.5),    # Ab (50)
    (3.5, 47, 90, 0.5),    # F (47)
    (3.75, 48, 90, 0.5),   # Gb (48)
    (4.25, 45, 90, 0.5),   # Eb (45)
    (4.75, 47, 90, 0.5),   # F (47)
    (5.0, 50, 90, 0.5),    # Ab (50)
    (5.5, 47, 90, 0.5),    # F (47)
    (5.75, 48, 90, 0.5),   # Gb (48)
    (6.0, 45, 90, 0.5)     # Eb (45)
]
for time, pitch, velocity, duration in bass_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + duration)
    bass.notes.append(note)

# Piano comping: 7th chords, on 2 and 4, with emotion
piano_notes = [
    (1.75, 64, 100, 0.25), # F7 (F, A, C, Eb)
    (1.75, 69, 100, 0.25),
    (1.75, 60, 100, 0.25),
    (1.75, 62, 100, 0.25),
    (2.25, 64, 100, 0.25),
    (2.25, 69, 100, 0.25),
    (2.25, 60, 100, 0.25),
    (2.25, 62, 100, 0.25),
    (3.25, 64, 100, 0.25),
    (3.25, 69, 100, 0.25),
    (3.25, 60, 100, 0.25),
    (3.25, 62, 100, 0.25),
    (4.25, 64, 100, 0.25),
    (4.25, 69, 100, 0.25),
    (4.25, 60, 100, 0.25),
    (4.25, 62, 100, 0.25),
    (5.25, 64, 100, 0.25),
    (5.25, 69, 100, 0.25),
    (5.25, 60, 100, 0.25),
    (5.25, 62, 100, 0.25),
]
for time, pitch, velocity, duration in piano_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + duration)
    piano.notes.append(note)

# Drums in bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    # Kick on 1
    kick = pretty_midi.Note(velocity=90, pitch=36, start=start, end=start + 0.125)
    drums.notes.append(kick)
    # Snare on 2
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.375 + 0.125)
    drums.notes.append(snare)
    # Hihat on 1 &
    hihat = pretty_midi.Note(velocity=60, pitch=42, start=start, end=start + 0.125)
    drums.notes.append(hihat)
    # Hihat on 2 &
    hihat = pretty_midi.Note(velocity=60, pitch=42, start=start + 0.375, end=start + 0.375 + 0.125)
    drums.notes.append(hihat)
    # Kick on 3
    kick = pretty_midi.Note(velocity=90, pitch=36, start=start + 0.75, end=start + 0.75 + 0.125)
    drums.notes.append(kick)
    # Snare on 4
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.125 + 0.125)
    drums.notes.append(snare)
    # Hihat on 3 &
    hihat = pretty_midi.Note(velocity=60, pitch=42, start=start + 0.75, end=start + 0.75 + 0.125)
    drums.notes.append(hihat)
    # Hihat on 4 &
    hihat = pretty_midi.Note(velocity=60, pitch=42, start=start + 1.125, end=start + 1.125 + 0.125)
    drums.notes.append(hihat)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
