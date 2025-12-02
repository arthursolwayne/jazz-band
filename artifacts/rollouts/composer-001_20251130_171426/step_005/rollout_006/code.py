
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
hihat = pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5)
hihat2 = pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75)
hihat3 = pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125)
hihat4 = pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5)

drums.notes.extend([kick, snare, hihat, hihat2, hihat3, hihat4])

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass: walking line, chromatic approaches, no repeated notes
# Dm7 = D F A C
# Walking bass line: D, F, G#, A, C, B, A, G
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=65, start=1.875, end=2.25), # F
    pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.625), # G#
    pretty_midi.Note(velocity=80, pitch=69, start=2.625, end=3.0),  # A
    pretty_midi.Note(velocity=80, pitch=72, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=80, pitch=71, start=3.375, end=3.75), # B
    pretty_midi.Note(velocity=80, pitch=69, start=3.75, end=4.125), # A
    pretty_midi.Note(velocity=80, pitch=67, start=4.125, end=4.5),  # G
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=80, pitch=65, start=4.875, end=5.25), # F
    pretty_midi.Note(velocity=80, pitch=67, start=5.25, end=5.625), # G#
    pretty_midi.Note(velocity=80, pitch=69, start=5.625, end=6.0),  # A
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
# Dm7 = D F A C
# Comp on beat 2 and 4 in each bar (1.875, 3.375, 4.875)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.25),  # D
    pretty_midi.Note(velocity=90, pitch=65, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=90, pitch=72, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=90, pitch=65, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=90, pitch=72, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=90, pitch=65, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=90, pitch=72, start=4.875, end=5.25),  # C
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm7 scale: D, Eb, F, G, A, Bb, C
# Motif: D, F, G, A -> D, F, G, A (reprise)
sax_notes = []
# Bar 2: D, F, G, A
sax_notes.append(pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75))  # D
sax_notes.append(pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=2.0))  # F
sax_notes.append(pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25))  # G
sax_notes.append(pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.5))  # A

# Bar 3: leave it hanging
# Bar 4: repeat the motif
sax_notes.append(pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75))  # D
sax_notes.append(pretty_midi.Note(velocity=100, pitch=65, start=4.75, end=5.0))  # F
sax_notes.append(pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.25))  # G
sax_notes.append(pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.5))  # A

sax.notes.extend(sax_notes)

# Drums: Continue kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bars 2-4: 1.5 to 6.0
for bar in range(2, 5):
    start = bar * 1.5
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    hihat = pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 1.5)
    hihat2 = pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat3 = pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat4 = pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick, snare, hihat, hihat2, hihat3, hihat4])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
