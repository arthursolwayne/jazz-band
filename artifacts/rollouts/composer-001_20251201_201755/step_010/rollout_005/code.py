
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
for beat in [0, 1, 2, 3]:
    note = pretty_midi.Note(velocity=100, pitch=42, start=beat * 0.375, end=beat * 0.375 + 0.1875)
    drums.notes.append(note)
for beat in [0, 2]:
    note = pretty_midi.Note(velocity=110, pitch=38, start=beat * 0.375, end=beat * 0.375 + 0.1875)
    drums.notes.append(note)
for beat in [0, 1, 2, 3]:
    note = pretty_midi.Note(velocity=80, pitch=36, start=beat * 0.375, end=beat * 0.375 + 0.1875)
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass line: walking line with chromatic approaches
bass_notes = [
    (1, 43),   # F
    (1.5, 42), # E
    (2, 44),   # F#
    (2.5, 43), # F
    (3, 45),   # G
    (3.5, 44), # F#
    (4, 47),   # A
    (4.5, 45), # G
    (5, 49),   # Bb
    (5.5, 47), # A
    (6, 50),   # B
    (6.5, 49), # Bb
]
for start, pitch in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + 0.5)
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    (1.5, 64), # F
    (1.5, 76), # A
    (1.5, 69), # C
    (1.5, 72), # E
]
for start, pitch in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 1.0)
    piano.notes.append(note)

# Bar 3: Bbmaj7 (Bb, D, F, Ab)
piano_notes = [
    (2.5, 71), # Bb
    (2.5, 74), # D
    (2.5, 64), # F
    (2.5, 76), # Ab
]
for start, pitch in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 1.0)
    piano.notes.append(note)

# Bar 4: Emaj7 (E, G#, B, D)
piano_notes = [
    (3.5, 72), # E
    (3.5, 76), # G#
    (3.5, 76), # B (same as G# but higher octave)
    (3.5, 69), # D
]
for start, pitch in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 1.0)
    piano.notes.append(note)

# Sax: Melody, one short motif, start it, leave it hanging, come back and finish it
# Motif: F, Bb, E, F (3 notes, leave the last one hanging)
sax_notes = [
    (1.5, 64), # F
    (1.75, 71), # Bb
    (2.0, 72), # E
    (2.25, 64), # F
    (3.0, 64), # F (come back and finish)
]
for start, pitch in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=start, end=start + 0.25)
    sax.notes.append(note)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("wayne_intro.mid")
