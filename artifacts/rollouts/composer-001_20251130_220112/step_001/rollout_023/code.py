
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
kick = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
snare = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)
hihat = pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5)
drums.notes.extend([kick, snare, hihat])

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, never the same note twice
# Dm7: D, F, A, C
# Root motion: D -> C -> B -> A
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.25), # C
    pretty_midi.Note(velocity=100, pitch=59, start=2.25, end=2.625), # B
    pretty_midi.Note(velocity=100, pitch=57, start=2.625, end=3.0),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=3.375, end=3.75), # C
    pretty_midi.Note(velocity=100, pitch=59, start=3.75, end=4.125), # B
    pretty_midi.Note(velocity=100, pitch=57, start=4.125, end=4.5),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.25), # C
    pretty_midi.Note(velocity=100, pitch=59, start=5.25, end=5.625), # B
    pretty_midi.Note(velocity=100, pitch=57, start=5.625, end=6.0),  # A
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
# Dm7 = D, F, A, C
# Root motion: D -> C -> B -> A
piano_notes = [
    # Bar 2 (1.5 - 3.0)
    pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=2.0),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),  # C
    # Bar 3 (3.0 - 4.5)
    pretty_midi.Note(velocity=100, pitch=60, start=3.25, end=3.5),  # C
    pretty_midi.Note(velocity=100, pitch=58, start=3.25, end=3.5),  # E
    pretty_midi.Note(velocity=100, pitch=65, start=3.25, end=3.5),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5),  # B
    # Bar 4 (4.5 - 6.0)
    pretty_midi.Note(velocity=100, pitch=57, start=4.75, end=5.0),  # B
    pretty_midi.Note(velocity=100, pitch=55, start=4.75, end=5.0),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=100, pitch=59, start=4.75, end=5.0),  # A
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bars 2-4
for bar in range(2, 5):
    start = bar * 1.5
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    hihat = pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 1.5)
    drums.notes.extend([kick, snare, hihat])

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D (62), F (64), A (67), G (65)
# Bar 2 (1.5 - 3.0)
note1 = pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75)
note2 = pretty_midi.Note(velocity=110, pitch=64, start=1.75, end=2.0)
note3 = pretty_midi.Note(velocity=110, pitch=67, start=2.0, end=2.25)
note4 = pretty_midi.Note(velocity=110, pitch=65, start=2.25, end=2.5)
note5 = pretty_midi.Note(velocity=110, pitch=62, start=2.5, end=2.75)
note6 = pretty_midi.Note(velocity=110, pitch=64, start=2.75, end=3.0)
sax.notes.extend([note1, note2, note3, note4, note5, note6])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
