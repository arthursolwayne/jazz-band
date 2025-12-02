
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
    start = bar * 1.5
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    hihat = pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 1.5)
    hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick, snare, hihat])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: walking line, chromatic approaches, no repeated notes
for bar in range(2, 5):
    start = bar * 1.5
    if bar == 2:
        notes = [62, 64, 65, 67]  # Dm7
    elif bar == 3:
        notes = [67, 69, 71, 72]  # G7
    else:
        notes = [72, 74, 76, 77]  # Cmaj7
    for i, note in enumerate(notes):
        bass_note = pretty_midi.Note(velocity=90, pitch=note, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        bass.notes.append(bass_note)

# Piano: 7th chords, comp on 2 and 4
for bar in range(2, 5):
    start = bar * 1.5
    if bar == 2:
        chords = [(62, 67), (64, 69)]  # Dm7
    elif bar == 3:
        chords = [(67, 72), (69, 74)]  # G7
    else:
        chords = [(72, 77), (74, 79)]  # Cmaj7
    for i, (root, seventh) in enumerate(chords):
        piano_note = pretty_midi.Note(velocity=90, pitch=root, start=start + i * 0.75, end=start + i * 0.75 + 0.25)
        piano.notes.append(piano_note)
        piano_note = pretty_midi.Note(velocity=70, pitch=seventh, start=start + i * 0.75, end=start + i * 0.75 + 0.25)
        piano.notes.append(piano_note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D, F, G, Bb (Dm7)
# Start at bar 2, first beat
sax_note = pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.5 + 0.375)
sax.notes.append(sax_note)
sax_note = pretty_midi.Note(velocity=110, pitch=64, start=1.5 + 0.75, end=1.5 + 0.75 + 0.375)
sax.notes.append(sax_note)
sax_note = pretty_midi.Note(velocity=110, pitch=67, start=1.5 + 1.125, end=1.5 + 1.125 + 0.375)
sax.notes.append(sax_note)
sax_note = pretty_midi.Note(velocity=110, pitch=66, start=3.0, end=3.0 + 0.75)
sax.notes.append(sax_note)
sax_note = pretty_midi.Note(velocity=110, pitch=67, start=3.0 + 0.75, end=3.0 + 0.75 + 0.375)
sax.notes.append(sax_note)
sax_note = pretty_midi.Note(velocity=110, pitch=69, start=3.0 + 1.125, end=3.0 + 1.125 + 0.375)
sax.notes.append(sax_note)
sax_note = pretty_midi.Note(velocity=110, pitch=72, start=4.5, end=4.5 + 0.375)
sax.notes.append(sax_note)

# Drums: continue for bars 2-4
for bar in range(2, 5):
    start = bar * 1.5
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    hihat = pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 1.5)
    hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick, snare, hihat])

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
