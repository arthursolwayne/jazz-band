
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hi-hat on every eighth
    hihat1 = pretty_midi.Note(velocity=90, pitch=42, start=start, end=start + 0.375)
    hihat2 = pretty_midi.Note(velocity=90, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat3 = pretty_midi.Note(velocity=90, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat4 = pretty_midi.Note(velocity=90, pitch=42, start=start + 1.125, end=start + 1.5)

    drums.notes.extend([kick1, kick2, snare1, snare2, hihat1, hihat2, hihat3, hihat4])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus, walking line, chromatic approaches, no repeated notes
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=63, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=80, pitch=65, start=2.25, end=2.625), # F
    pretty_midi.Note(velocity=80, pitch=67, start=2.625, end=3.0),  # G
    pretty_midi.Note(velocity=80, pitch=69, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=80, pitch=70, start=3.375, end=3.75), # Bb
    pretty_midi.Note(velocity=80, pitch=72, start=3.75, end=4.125), # B
    pretty_midi.Note(velocity=80, pitch=74, start=4.125, end=4.5),  # C
    pretty_midi.Note(velocity=80, pitch=76, start=4.5, end=4.875),  # C#
    pretty_midi.Note(velocity=80, pitch=77, start=4.875, end=5.25), # D
    pretty_midi.Note(velocity=80, pitch=79, start=5.25, end=5.625), # Eb
    pretty_midi.Note(velocity=80, pitch=81, start=5.625, end=6.0),  # F
]
bass.notes.extend(bass_notes)

# Piano: Diane, 7th chords, comp on 2 and 4
# D7, Bm7b5, G7, C7
piano_notes = []

# Bar 2 (1.5 - 3.0s)
# D7: D, F#, A, C
for note in [62, 67, 71, 72]:
    piano_notes.append(pretty_midi.Note(velocity=100, pitch=note, start=1.5, end=1.875))
for note in [62, 67, 71, 72]:
    piano_notes.append(pretty_midi.Note(velocity=100, pitch=note, start=2.25, end=2.625))

# Bar 3 (3.0 - 4.5s)
# Bm7b5: B, D, F, A
for note in [71, 67, 64, 71]:
    piano_notes.append(pretty_midi.Note(velocity=100, pitch=note, start=3.0, end=3.375))
for note in [71, 67, 64, 71]:
    piano_notes.append(pretty_midi.Note(velocity=100, pitch=note, start=3.75, end=4.125))

# Bar 4 (4.5 - 6.0s)
# G7: G, B, D, F
for note in [74, 77, 79, 71]:
    piano_notes.append(pretty_midi.Note(velocity=100, pitch=note, start=4.5, end=4.875))
for note in [74, 77, 79, 71]:
    piano_notes.append(pretty_midi.Note(velocity=100, pitch=note, start=5.25, end=5.625))

piano.notes.extend(piano_notes)

# Sax: Dante, one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D (62), E (64), F# (67), D (62)

note1 = pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875)
note2 = pretty_midi.Note(velocity=110, pitch=64, start=1.875, end=2.25)
note3 = pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.625)
note4 = pretty_midi.Note(velocity=110, pitch=62, start=3.375, end=3.75)

sax.notes.extend([note1, note2, note3, note4])

# Drums for bars 2-4
for bar in range(2, 4):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hi-hat on every eighth
    hihat1 = pretty_midi.Note(velocity=90, pitch=42, start=start, end=start + 0.375)
    hihat2 = pretty_midi.Note(velocity=90, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat3 = pretty_midi.Note(velocity=90, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat4 = pretty_midi.Note(velocity=90, pitch=42, start=start + 1.125, end=start + 1.5)

    drums.notes.extend([kick1, kick2, snare1, snare2, hihat1, hihat2, hihat3, hihat4])

midi.instruments.extend([sax, bass, piano, drums])
midi.write("jazz_intro.mid")
