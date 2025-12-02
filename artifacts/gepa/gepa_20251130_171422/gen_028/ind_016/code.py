
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    # Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375), # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75), # Snare
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375), # Hihat
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75), # Hihat
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125), # Hihat
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5), # Hihat
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5), # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875), # Snare
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Everyone in. Sax takes melody
# Start with a short motif on sax: Fm7 -> Bb -> Eb -> F (Fm scale)
# 4 notes, one per beat
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.25), # Bb
    pretty_midi.Note(velocity=100, pitch=57, start=2.25, end=2.625), # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=3.0), # F
]
for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line in Fm, chromatic approach
# F -> Gb -> G -> Ab -> A -> Bb -> B -> C -> D -> Eb -> F
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=47, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=100, pitch=48, start=1.875, end=2.25), # Gb
    pretty_midi.Note(velocity=100, pitch=49, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=100, pitch=50, start=2.625, end=3.0), # Ab
    pretty_midi.Note(velocity=100, pitch=51, start=3.0, end=3.375), # A
    pretty_midi.Note(velocity=100, pitch=52, start=3.375, end=3.75), # Bb
    pretty_midi.Note(velocity=100, pitch=53, start=3.75, end=4.125), # B
    pretty_midi.Note(velocity=100, pitch=55, start=4.125, end=4.5), # C
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=4.875), # D
    pretty_midi.Note(velocity=100, pitch=59, start=4.875, end=5.25), # Eb
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.625), # F
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
# Fm7 = F, Ab, Bb, Db
# Cm7 = C, Eb, F, G
piano_notes = [
    # Bar 2: Fm7 on beat 2
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25), # F
    pretty_midi.Note(velocity=100, pitch=59, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.25), # F
    pretty_midi.Note(velocity=100, pitch=61, start=1.875, end=2.25), # G
    # Bar 3: Cm7 on beat 2
    pretty_midi.Note(velocity=100, pitch=60, start=3.375, end=3.75), # C
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75), # E
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.75), # F
    pretty_midi.Note(velocity=100, pitch=66, start=3.375, end=3.75), # G
    # Bar 4: Fm7 on beat 2
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25), # F
    pretty_midi.Note(velocity=100, pitch=59, start=4.875, end=5.25), # Eb
    pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.25), # F
    pretty_midi.Note(velocity=100, pitch=61, start=4.875, end=5.25), # G
]
for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Drums
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i in range(1, 4):
    start = 1.5 + i * 1.5
    # Kick
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    # Snare
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    # Hihat
    pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75)
    pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125)
    pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5)

# Bar 4: Drums
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i in range(3, 4):
    start = 1.5 + i * 1.5
    # Kick
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    # Snare
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    # Hihat
    pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75)
    pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125)
    pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5)

# Bar 2: Sax continues with second motif (variation)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375), # F
    pretty_midi.Note(velocity=100, pitch=60, start=3.375, end=3.75), # Bb
    pretty_midi.Note(velocity=100, pitch=57, start=3.75, end=4.125), # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=4.125, end=4.5), # F
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Sax continues with third motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875), # F
    pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.25), # Bb
    pretty_midi.Note(velocity=100, pitch=57, start=5.25, end=5.625), # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=6.0), # F
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Drums
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i in range(3, 4):
    start = 1.5 + i * 1.5
    # Kick
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    # Snare
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    # Hihat
    pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75)
    pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125)
    pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("intro.mid")
