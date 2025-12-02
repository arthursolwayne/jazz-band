
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
kick_times = [0.0, 0.75, 1.5, 2.25, 3.0, 3.75, 4.5, 5.25]
snare_times = [0.375, 1.125, 1.875, 2.625, 3.375, 4.125, 4.875]
hihat_times = [0.0, 0.1875, 0.375, 0.5625, 0.75, 0.9375, 1.125, 1.3125,
               1.5, 1.6875, 1.875, 2.0625, 2.25, 2.4375, 2.625, 2.8125,
               3.0, 3.1875, 3.375, 3.5625, 3.75, 3.9375, 4.125, 4.3125,
               4.5, 4.6875, 4.875, 5.0625, 5.25, 5.4375]

for t in kick_times:
    note = pretty_midi.Note(velocity=100, pitch=36, start=t, end=t + 0.125)
    drums.notes.append(note)

for t in snare_times:
    note = pretty_midi.Note(velocity=110, pitch=38, start=t, end=t + 0.125)
    drums.notes.append(note)

for t in hihat_times:
    note = pretty_midi.Note(velocity=80, pitch=42, start=t, end=t + 0.0625)
    drums.notes.append(note)

# Bar 2: Everyone in (1.5 - 3.0s)

# Marcus: Walking line in Fm (F, Gb, Ab, Bb), chromatic approaches
bass_notes = [
    (1.5, 53),  # F
    (1.75, 51),  # Eb
    (2.0, 52),  # F
    (2.25, 50),  # Db
    (2.5, 51),  # Eb
    (2.75, 48),  # Bb
    (3.0, 53),  # F
]

for t, pitch in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=t, end=t + 0.25)
    bass.notes.append(note)

# Diane: 7th chords on 2 and 4 (bars 2 and 3)
piano_notes = [
    # Bar 2: Fm7 on beat 2
    (1.75, 53),  # F
    (1.75, 48),  # Bb
    (1.75, 50),  # Db
    (1.75, 51),  # Eb
    # Bar 3: Bb7 on beat 4
    (3.0, 50),  # Bb
    (3.0, 46),  # Eb
    (3.0, 48),  # G
    (3.0, 51),  # Bb
]

for t, pitch in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=t, end=t + 0.125)
    piano.notes.append(note)

# Dante: Tenor sax motif, 4-note phrase starting on beat 2, ends on beat 4
# Fm scale: F, Gb, Ab, Bb, C, Db, Eb
sax_notes = [
    (1.75, 53),  # F
    (2.0, 51),   # Eb
    (2.25, 50),  # Db
    (2.5, 48),   # Bb
]

for t, pitch in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=t, end=t + 0.25)
    sax.notes.append(note)

# Bar 3: Everyone in (3.0 - 4.5s)

# Marcus: Walking line in Fm (F, Gb, Ab, Bb), chromatic approaches
bass_notes = [
    (3.0, 53),  # F
    (3.25, 51),  # Eb
    (3.5, 52),  # F
    (3.75, 50),  # Db
    (4.0, 51),  # Eb
    (4.25, 48),  # Bb
    (4.5, 53),  # F
]

for t, pitch in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=t, end=t + 0.25)
    bass.notes.append(note)

# Diane: 7th chords on 2 and 4 (bars 3 and 4)
piano_notes = [
    # Bar 3: Bb7 on beat 2
    (3.25, 50),  # Bb
    (3.25, 46),  # Eb
    (3.25, 48),  # G
    (3.25, 51),  # Bb
    # Bar 4: Fm7 on beat 4
    (4.5, 53),  # F
    (4.5, 48),  # Bb
    (4.5, 50),  # Db
    (4.5, 51),  # Eb
]

for t, pitch in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=t, end=t + 0.125)
    piano.notes.append(note)

# Dante: Tenor sax motif, 4-note phrase starting on beat 2, ends on beat 4
# Fm scale: F, Gb, Ab, Bb, C, Db, Eb
sax_notes = [
    (3.25, 50),  # Db
    (3.5, 48),   # Bb
    (3.75, 51),  # Eb
    (4.0, 53),   # F
]

for t, pitch in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=t, end=t + 0.25)
    sax.notes.append(note)

# Bar 4: Everyone in (4.5 - 6.0s)

# Marcus: Walking line in Fm (F, Gb, Ab, Bb), chromatic approaches
bass_notes = [
    (4.5, 53),  # F
    (4.75, 51),  # Eb
    (5.0, 52),  # F
    (5.25, 50),  # Db
    (5.5, 51),  # Eb
    (5.75, 48),  # Bb
    (6.0, 53),  # F
]

for t, pitch in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=t, end=t + 0.25)
    bass.notes.append(note)

# Diane: 7th chords on beat 2 and 4 (bar 4)
piano_notes = [
    # Bar 4: Fm7 on beat 2
    (4.75, 53),  # F
    (4.75, 48),  # Bb
    (4.75, 50),  # Db
    (4.75, 51),  # Eb
]

for t, pitch in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=t, end=t + 0.125)
    piano.notes.append(note)

# Dante: Tenor sax motif, 4-note phrase starting on beat 2, ends on beat 4
# Fm scale: F, Gb, Ab, Bb, C, Db, Eb
sax_notes = [
    (4.75, 53),  # F
    (5.0, 51),   # Eb
    (5.25, 50),  # Db
    (5.5, 48),   # Bb
]

for t, pitch in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=t, end=t + 0.25)
    sax.notes.append(note)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
