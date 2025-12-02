
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
kick_notes = [36, 36, 36, 36]
snare_notes = [38, 38, 38, 38]
hihat_notes = [42] * 8

# Create notes for bar 1
for i in range(4):
    kick = pretty_midi.Note(velocity=100, pitch=kick_notes[i], start=i * 0.375, end=(i + 1) * 0.375)
    snare = pretty_midi.Note(velocity=100, pitch=snare_notes[i], start=(i + 1) * 0.375, end=(i + 2) * 0.375)
    drums.notes.append(kick)
    drums.notes.append(snare)

for i in range(8):
    hihat = pretty_midi.Note(velocity=80, pitch=hihat_notes[i], start=i * 0.1875, end=(i + 1) * 0.1875)
    drums.notes.append(hihat)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line in Dm, chromatic approaches, no repeated notes
bass_notes = [50, 49, 48, 50, 52, 51, 50, 48, 47, 48, 50, 52, 51, 50, 48, 47]
for i in range(16):
    note = pretty_midi.Note(velocity=80, pitch=bass_notes[i], start=(i * 0.375) + 1.5, end=(i + 1) * 0.375 + 1.5)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
# Dm7 = D F A C
# Use rootless voicings, comp on beats 2 and 4

piano_notes = [
    # Bar 2
    62, 64, 67, 72,  # Dm7 (G B D F)
    64, 67, 72, 76,  # F7 (A C E G)
    # Bar 3
    67, 69, 72, 76,  # A7 (C E G B)
    69, 72, 76, 79,  # B7 (D F# A C#)
    # Bar 4
    62, 64, 67, 72,  # Dm7 (G B D F)
    64, 67, 72, 76   # F7 (A C E G)
]

for i in range(len(piano_notes)):
    note = pretty_midi.Note(velocity=100, pitch=piano_notes[i], start=(i // 4 * 1.5) + ((i % 4) * 0.375) + 1.5, end=(i // 4 * 1.5) + ((i % 4) * 0.375) + 1.5 + 0.1875)
    piano.notes.append(note)

# Sax: Short motif, make it sing
# Dm scale: D, Eb, F, G, A, Bb, C
# Motif: D (F), G (Bb), A (C), leave it hanging on Bb

sax_notes = [
    (62, 0.375),  # D
    (64, 0.1875), # Eb
    (67, 0.1875), # F
    (69, 0.1875), # G
    (71, 0.1875), # A
    (70, 0.1875), # Bb
    (74, 0.1875)  # C
]

for i, (pitch, duration) in enumerate(sax_notes):
    start = 1.5 + (i * 0.1875)
    end = start + duration
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=start, end=end)
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
