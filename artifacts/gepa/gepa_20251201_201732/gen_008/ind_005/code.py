
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
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat % 2 == 0:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        else:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (F2, Ab2, Bb2, Db3, etc.) with chromatic approaches
bass_notes = [
    (1.5, 38, 0.25),   # F2
    (1.75, 40, 0.25),  # Gb2
    (2.0, 41, 0.25),   # G2
    (2.25, 43, 0.25),  # Ab2
    (2.5, 44, 0.25),   # A2
    (2.75, 45, 0.25),  # Bb2
    (3.0, 47, 0.25),   # B2
    (3.25, 48, 0.25),  # C3
    (3.5, 43, 0.25),   # Ab2
    (3.75, 45, 0.25),  # Bb2
    (4.0, 47, 0.25),   # B2
    (4.25, 48, 0.25),  # C3
    (4.5, 50, 0.25),   # Db3
    (4.75, 52, 0.25),  # D3
    (5.0, 53, 0.25),   # Eb3
    (5.25, 55, 0.25),  # E3
    (5.5, 55, 0.25),   # E3
    (5.75, 52, 0.25)   # D3
]
for time, pitch, duration in bass_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + duration)
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, Eb)
piano_notes = [
    (1.5, 53, 0.25),  # F3
    (1.5, 55, 0.25),  # G3
    (1.5, 58, 0.25),  # A3
    (1.5, 60, 0.25),  # Bb3
    # Bar 3: Bb7 (Bb, D, F, Ab)
    (2.0, 58, 0.25),  # Bb3
    (2.0, 62, 0.25),  # D4
    (2.0, 53, 0.25),  # F3
    (2.0, 55, 0.25),  # G3
    # Bar 4: Cm7 (C, Eb, G, Bb)
    (2.5, 60, 0.25),  # C4
    (2.5, 63, 0.25),  # Eb4
    (2.5, 67, 0.25),  # G4
    (2.5, 69, 0.25),  # Bb4
    # Final resolution: Fm7 (F, Ab, C, Eb)
    (3.0, 53, 0.25),  # F3
    (3.0, 55, 0.25),  # G3
    (3.0, 58, 0.25),  # A3
    (3.0, 60, 0.25),  # Bb3
]
for time, pitch, duration in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + duration)
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm motif: F, Eb, G, F
sax_notes = [
    (1.5, 53, 0.375),  # F3
    (1.875, 60, 0.375),  # Eb3
    (2.25, 58, 0.375),  # G3
    (2.625, 53, 0.375),  # F3
    (3.0, 53, 0.375),  # F3
    (3.375, 55, 0.375),  # G3
    (3.75, 58, 0.375),  # A3
    (4.125, 53, 0.375)   # F3
]
for time, pitch, duration in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=time, end=time + duration)
    sax.notes.append(note)

# Drums: Full bar
for bar in range(2, 4):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat % 2 == 0:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        else:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
