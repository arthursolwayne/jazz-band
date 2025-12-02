
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
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125))
        if beat == 1 or beat == 3:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125))
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: walking line, chromatic approaches
# D minor scale: D, Eb, F, G, Ab, Bb, C
bass_notes = [
    # Bar 2
    50, 49, 51, 47,  # D, Eb, F, G
    # Bar 3
    45, 48, 50, 52,  # Ab, Bb, C, D
    # Bar 4
    51, 53, 50, 47,  # F, G, D, G
]
for i, note in enumerate(bass_notes):
    time = 1.5 + (i // 4) * 1.5 + (i % 4) * 0.375
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Diane on piano: 7th chords, comp on 2 and 4
# D7 (D, F#, A, C)
# G7 (G, Bb, D, F)
# C7 (C, E, G, Bb)
# A7 (A, C#, E, G)
piano_notes = [
    # Bar 2, beat 2 (D7)
    52, 56, 59, 60,
    # Bar 3, beat 2 (G7)
    62, 65, 67, 69,
    # Bar 4, beat 2 (A7)
    65, 68, 72, 76,
]
for i, note in enumerate(piano_notes):
    time = 1.5 + (i // 2) * 1.5 + (i % 2) * 1.5 + 0.75
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# You on sax: one short motif, make it sing
# D, Eb, F, C (intervallic movement with space)
sax_notes = [
    # Bar 2, beat 1: D
    62,
    # Bar 2, beat 2: Eb
    63,
    # Bar 2, beat 3: F
    64,
    # Bar 2, beat 4: rest
    # Bar 3, beat 1: rest
    # Bar 3, beat 2: C
    60,
    # Bar 3, beat 3: F
    64,
    # Bar 3, beat 4: D
    62,
    # Bar 4, beat 1: Eb
    63,
    # Bar 4, beat 2: F
    64,
    # Bar 4, beat 3: C
    60,
    # Bar 4, beat 4: rest
]
for i, note in enumerate(sax_notes):
    time = 1.5 + (i // 4) * 1.5 + (i % 4) * 0.375
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25))

# Little Ray on drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    for beat in range(4):
        time = 1.5 + bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125))
        if beat == 1 or beat == 3:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125))
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
