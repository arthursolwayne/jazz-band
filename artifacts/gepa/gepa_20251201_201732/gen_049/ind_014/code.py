
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
    time = bar * 1.5
    # Kick on 1
    kick = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.375)
    drums.notes.append(kick)
    # Snare on 2
    snare = pretty_midi.Note(velocity=100, pitch=38, start=time + 0.75, end=time + 0.75 + 0.375)
    drums.notes.append(snare)
    # Hihat on every eighth
    for i in range(4):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=time + i * 0.375, end=time + i * 0.375 + 0.125)
        drums.notes.append(hihat)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Dm, roots and fifths with chromatic approaches
for bar in range(2, 5):
    time = bar * 1.5
    # Dm root
    note = pretty_midi.Note(velocity=90, pitch=50, start=time, end=time + 0.375)
    bass.notes.append(note)
    # Chromatic approach up to G
    note = pretty_midi.Note(velocity=90, pitch=51, start=time + 0.375, end=time + 0.75)
    bass.notes.append(note)
    # G (fifth)
    note = pretty_midi.Note(velocity=90, pitch=55, start=time + 0.75, end=time + 1.125)
    bass.notes.append(note)
    # Chromatic approach down to D
    note = pretty_midi.Note(velocity=90, pitch=54, start=time + 1.125, end=time + 1.5)
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (F, A, D, F#)
for i, pitch in enumerate([65, 68, 72, 76]):
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=1.5, end=1.5 + 0.75)
    piano.notes.append(note)

# Bar 3: G7 (B, D, G, B)
for i, pitch in enumerate([71, 74, 78, 82]):
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=3.0, end=3.0 + 0.75)
    piano.notes.append(note)

# Bar 4: Cm7 (E, G, C, E)
for i, pitch in enumerate([64, 67, 72, 76]):
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=4.5, end=4.5 + 0.75)
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: Dm (D, F, G, Bb) with a slight chromatic run
# Bar 2
note = pretty_midi.Note(velocity=110, pitch=72, start=1.5, end=1.5 + 0.375)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=74, start=1.875, end=1.875 + 0.375)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=76, start=2.25, end=2.25 + 0.375)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=71, start=2.625, end=2.625 + 0.375)
sax.notes.append(note)

# Bar 3
note = pretty_midi.Note(velocity=110, pitch=72, start=3.0, end=3.0 + 0.375)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=74, start=3.375, end=3.375 + 0.375)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=76, start=3.75, end=3.75 + 0.375)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=71, start=4.125, end=4.125 + 0.375)
sax.notes.append(note)

# Bar 4
note = pretty_midi.Note(velocity=110, pitch=72, start=4.5, end=4.5 + 0.375)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=74, start=4.875, end=4.875 + 0.375)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=76, start=5.25, end=5.25 + 0.375)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=71, start=5.625, end=6.0)
sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Write the MIDI file
# midi.write disabled
