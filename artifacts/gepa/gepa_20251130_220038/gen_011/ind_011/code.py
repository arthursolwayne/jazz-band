
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    start = bar * 1.5
    # Kick on 1 and 3
    kick_time = start + 0.0
    kick = pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.1)
    drums.notes.append(kick)
    kick_time = start + 0.75
    kick = pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.1)
    drums.notes.append(kick)
    # Snare on 2 and 4
    snare_time = start + 0.375
    snare = pretty_midi.Note(velocity=110, pitch=38, start=snare_time, end=snare_time + 0.1)
    drums.notes.append(snare)
    snare_time = start + 1.125
    snare = pretty_midi.Note(velocity=110, pitch=38, start=snare_time, end=snare_time + 0.1)
    drums.notes.append(snare)
    # Hihat on every eighth
    for i in range(8):
        hihat_time = start + i * 0.375
        hihat = pretty_midi.Note(velocity=90, pitch=42, start=hihat_time, end=hihat_time + 0.05)
        drums.notes.append(hihat)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    (1.5, 62),   # D4
    (1.875, 63), # Eb4
    (2.25, 64),  # E4
    (2.625, 65), # F4
    (3.0, 67),   # G4
    (3.375, 69), # A4
    (3.75, 70),  # Bb4
    (4.125, 71), # B4
    (4.5, 72),   # C5
    (4.875, 71), # B4
    (5.25, 70),  # Bb4
    (5.625, 69), # A4
    (6.0, 67)    # G4
]
for time, pitch in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (1.875, 62, 67),   # D7 (D, F#, A, C#)
    (2.25, 62, 67),
    (3.0, 64, 69),     # E7 (E, G#, B, D)
    (3.375, 64, 69),
    (4.5, 67, 72),     # G7 (G, B, D, F#)
    (4.875, 67, 72)
]
for time, root, seventh in piano_notes:
    # 7th chord: root, major 3rd, perfect 5th, 7th
    if seventh == 67:  # D7
        notes = [62, 67, 72, 74]
    elif seventh == 69:  # E7
        notes = [64, 69, 76, 79]
    elif seventh == 72:  # G7
        notes = [67, 72, 76, 81]
    for pitch in notes:
        note = pretty_midi.Note(velocity=95, pitch=pitch, start=time, end=time + 0.25)
        piano.notes.append(note)

# Sax: Motif, make it sing. Start it, leave it hanging, come back and finish it.
sax_notes = [
    (1.5, 65),   # E4
    (1.75, 67),  # G4
    (2.0, 64),   # E4
    (2.25, 67),  # G4
    (2.5, 65),   # E4
    (2.75, 67),  # G4
    (3.0, 64),   # E4
    (3.25, 69),  # A4
    (3.5, 67),   # G4
    (3.75, 64),  # E4
    (4.0, 65),   # E4
    (4.25, 67),  # G4
    (4.5, 64),   # E4
    (4.75, 67),  # G4
    (5.0, 65),   # E4
    (5.25, 69),  # A4
    (5.5, 67),   # G4
    (5.75, 64),  # E4
    (6.0, 62)    # D4
]
for time, pitch in sax_notes:
    note = pretty_midi.Note(velocity=105, pitch=pitch, start=time, end=time + 0.25)
    sax.notes.append(note)

# Drums for bars 2-4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    kick_time = start + 0.0
    kick = pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.1)
    drums.notes.append(kick)
    kick_time = start + 0.75
    kick = pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.1)
    drums.notes.append(kick)
    # Snare on 2 and 4
    snare_time = start + 0.375
    snare = pretty_midi.Note(velocity=110, pitch=38, start=snare_time, end=snare_time + 0.1)
    drums.notes.append(snare)
    snare_time = start + 1.125
    snare = pretty_midi.Note(velocity=110, pitch=38, start=snare_time, end=snare_time + 0.1)
    drums.notes.append(snare)
    # Hihat on every eighth
    for i in range(8):
        hihat_time = start + i * 0.375
        hihat = pretty_midi.Note(velocity=90, pitch=42, start=hihat_time, end=hihat_time + 0.05)
        drums.notes.append(hihat)

midi.instruments.extend([sax, bass, piano, drums])

# Save MIDI
midi.write("dante_intro.mid")
