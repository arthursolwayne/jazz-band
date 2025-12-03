
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
for bar in range(1):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=110, pitch=38, start=time, end=time + 0.1)
            drums.notes.append(note)
        # Hi-Hat on every eighth
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.05)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line, roots and fifths with chromatic approaches
bass_notes = [
    (1.5, 50, 0.25),  # D2 (root)
    (1.75, 51, 0.25), # Eb2 (chromatic approach)
    (2.0, 52, 0.25),  # E2 (fifth)
    (2.25, 50, 0.25), # D2 (root)
    (2.5, 53, 0.25),  # F2 (chromatic approach)
    (2.75, 55, 0.25), # G2 (fifth)
    (3.0, 57, 0.25),  # A2 (root)
    (3.25, 58, 0.25), # Bb2 (chromatic)
    (3.5, 59, 0.25),  # B2 (fifth)
    (3.75, 57, 0.25), # A2 (root)
    (4.0, 60, 0.25),  # B2 (chromatic)
    (4.25, 62, 0.25), # C#3 (fifth)
    (4.5, 64, 0.25),  # D3 (root)
    (4.75, 65, 0.25), # Eb3 (chromatic)
    (5.0, 66, 0.25),  # E3 (fifth)
    (5.25, 64, 0.25), # D3 (root)
]

for time, pitch, duration in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + duration)
    bass.notes.append(note)

# Piano: open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D F# A C#)
piano_notes = []
for time in [1.5, 1.75, 2.0, 2.25]:
    piano_notes.append(pretty_midi.Note(velocity=90, pitch=62, start=time, end=time + 0.25))  # D3
    piano_notes.append(pretty_midi.Note(velocity=90, pitch=67, start=time, end=time + 0.25))  # F#3
    piano_notes.append(pretty_midi.Note(velocity=90, pitch=71, start=time, end=time + 0.25))  # A3
    piano_notes.append(pretty_midi.Note(velocity=90, pitch=76, start=time, end=time + 0.25))  # C#4
piano.notes.extend(piano_notes)

# Bar 3: G7 (G B D F)
piano_notes = []
for time in [2.5, 2.75, 3.0, 3.25]:
    piano_notes.append(pretty_midi.Note(velocity=90, pitch=67, start=time, end=time + 0.25))  # G3
    piano_notes.append(pretty_midi.Note(velocity=90, pitch=71, start=time, end=time + 0.25))  # B3
    piano_notes.append(pretty_midi.Note(velocity=90, pitch=74, start=time, end=time + 0.25))  # D4
    piano_notes.append(pretty_midi.Note(velocity=90, pitch=78, start=time, end=time + 0.25))  # F4
piano.notes.extend(piano_notes)

# Bar 4: Bm7 (B D F# A)
piano_notes = []
for time in [3.5, 3.75, 4.0, 4.25]:
    piano_notes.append(pretty_midi.Note(velocity=90, pitch=71, start=time, end=time + 0.25))  # B3
    piano_notes.append(pretty_midi.Note(velocity=90, pitch=74, start=time, end=time + 0.25))  # D4
    piano_notes.append(pretty_midi.Note(velocity=90, pitch=77, start=time, end=time + 0.25))  # F#4
    piano_notes.append(pretty_midi.Note(velocity=90, pitch=81, start=time, end=time + 0.25))  # A4
piano.notes.extend(piano_notes)

# Sax: short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4 -> E4 -> D4 -> F#4 -> G4 -> A4
# First part (start to hang): D4, E4, D4
# Second part (come back): F#4, G4, A4

sax_notes = [
    (1.5, 62, 0.25),  # D4
    (1.75, 64, 0.25),  # E4
    (2.0, 62, 0.25),  # D4
    (3.5, 67, 0.25),  # F#4
    (3.75, 69, 0.25),  # G4
    (4.0, 71, 0.25),  # A4
]
for time, pitch, duration in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + duration)
    sax.notes.append(note)

# Drums continue for bars 2-4
for bar in range(2, 4):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=110, pitch=38, start=time, end=time + 0.1)
            drums.notes.append(note)
        # Hi-Hat on every eighth
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.05)
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
