
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
bar_length = 1.5
for bar in range(1):
    start = bar * bar_length
    # Kick on 1 and 3
    kick_1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick_3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare_2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare_4 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hi-hat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)
    drums.notes.extend([kick_1, kick_3, snare_2, snare_4])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, no repeated notes
# Dm7: D F A C
# Bass line: D -> Eb -> F -> G -> A -> Bb -> B -> C -> D
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=100, pitch=63, start=1.75, end=2.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=2.0, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.5),  # G
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=2.75),  # A
    pretty_midi.Note(velocity=100, pitch=68, start=2.75, end=3.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.25),  # B
    pretty_midi.Note(velocity=100, pitch=71, start=3.25, end=3.5),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=63, start=3.75, end=4.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=4.0, end=4.25),  # F
    pretty_midi.Note(velocity=100, pitch=65, start=4.25, end=4.5),  # G
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.75),  # A
    pretty_midi.Note(velocity=100, pitch=68, start=4.75, end=5.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=5.0, end=5.25),  # B
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.5),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=5.75),  # D
    pretty_midi.Note(velocity=100, pitch=63, start=5.75, end=6.0),  # Eb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
# Dm7 = D F A C
# Chord on beat 2 (1.75s) and 4 (2.25s, 2.75s, 3.25s, etc.)
def add_piano_chord(start, chord):
    for note in chord:
        piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.25))
chord_Dm7 = [62, 65, 67, 71]
for bar in range(2, 5):
    start = bar * bar_length
    add_piano_chord(start + 0.375, chord_Dm7)
    add_piano_chord(start + 0.75, chord_Dm7)
    add_piano_chord(start + 1.125, chord_Dm7)
    add_piano_chord(start + 1.5, chord_Dm7)

# Drums: Same pattern as bar 1, but repeated for bars 2-4
for bar in range(2, 5):
    start = bar * bar_length
    # Kick on 1 and 3
    kick_1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick_3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare_2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare_4 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hi-hat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)
    drums.notes.extend([kick_1, kick_3, snare_2, snare_4])

# Sax: Motif
# Dm7: D, F, A, C
# Motif: D -> F -> A -> C -> D (hanging on A)
# Start bar 2
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.5),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.75),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=2.75, end=3.0),  # A (hanging)
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # D (coming back)
    pretty_midi.Note(velocity=100, pitch=65, start=3.25, end=3.5),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.0),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=4.0, end=4.25),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=4.25, end=4.5),  # A (hanging)
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # D (coming back)
    pretty_midi.Note(velocity=100, pitch=65, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.25),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.5),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=5.75),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=5.75, end=6.0),  # A (hanging)
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_russo_intro.mid")
