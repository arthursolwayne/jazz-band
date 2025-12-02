
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
drum_notes = []
for bar in range(1):
    start = bar * 1.5
    # Kick on 1 and 3
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375))
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5))
    # Snare on 2 and 4
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125))
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.875))
    # Hi-hat on every eighth
    for i in range(8):
        drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875))

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches, not scales.
bass_notes = []
for bar in range(2, 5):
    start = bar * 1.5
    # Fm7: F, C, Ab, D
    # Walking bass line in Fm
    # Root on 1, 5th on 2, chromatic on 3, root on 4
    bass_notes.append(pretty_midi.Note(velocity=90, pitch=38, start=start + 0.0, end=start + 0.375))  # F2
    bass_notes.append(pretty_midi.Note(velocity=90, pitch=43, start=start + 0.75, end=start + 1.125))  # C3
    bass_notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start + 1.125, end=start + 1.5))  # Bb2
    bass_notes.append(pretty_midi.Note(velocity=90, pitch=38, start=start + 1.5, end=start + 1.875))  # F2

for note in bass_notes:
    bass.notes.append(note)

# Diane on piano: Open voicings, different chord each bar, resolve on the last. Comp on 2 and 4.
piano_notes = []
bar = 2
start = bar * 1.5
# Bar 2: Fm7 (F, Ab, C, Eb)
piano_notes.append(pretty_midi.Note(velocity=100, pitch=53, start=start + 0.0, end=start + 0.375))  # F4
piano_notes.append(pretty_midi.Note(velocity=100, pitch=48, start=start + 0.0, end=start + 0.375))  # Ab4
piano_notes.append(pretty_midi.Note(velocity=100, pitch=55, start=start + 0.0, end=start + 0.375))  # C5
piano_notes.append(pretty_midi.Note(velocity=100, pitch=50, start=start + 0.0, end=start + 0.375))  # Eb4

bar = 3
start = bar * 1.5
# Bar 3: Gm7 (G, Bb, D, F)
piano_notes.append(pretty_midi.Note(velocity=100, pitch=55, start=start + 0.0, end=start + 0.375))  # G4
piano_notes.append(pretty_midi.Note(velocity=100, pitch=50, start=start + 0.0, end=start + 0.375))  # Bb4
piano_notes.append(pretty_midi.Note(velocity=100, pitch=57, start=start + 0.0, end=start + 0.375))  # D5
piano_notes.append(pretty_midi.Note(velocity=100, pitch=53, start=start + 0.0, end=start + 0.375))  # F5

bar = 4
start = bar * 1.5
# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes.append(pretty_midi.Note(velocity=100, pitch=55, start=start + 0.0, end=start + 0.375))  # C5
piano_notes.append(pretty_midi.Note(velocity=100, pitch=50, start=start + 0.0, end=start + 0.375))  # Eb5
piano_notes.append(pretty_midi.Note(velocity=100, pitch=57, start=start + 0.0, end=start + 0.375))  # G5
piano_notes.append(pretty_midi.Note(velocity=100, pitch=52, start=start + 0.0, end=start + 0.375))  # Bb5

for note in piano_notes:
    piano.notes.append(note)

# You on sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = []
bar = 2
start = bar * 1.5
# Motif: F, Ab, Bbb (Bb), E
sax_notes.append(pretty_midi.Note(velocity=110, pitch=65, start=start + 0.0, end=start + 0.375))  # F5
sax_notes.append(pretty_midi.Note(velocity=110, pitch=62, start=start + 0.375, end=start + 0.75))  # Ab5
sax_notes.append(pretty_midi.Note(velocity=110, pitch=60, start=start + 0.75, end=start + 1.125))  # Bbb5 (Bb5)
sax_notes.append(pretty_midi.Note(velocity=110, pitch=65, start=start + 1.5, end=start + 1.875))  # F5

for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("jazz_piece.mid")
