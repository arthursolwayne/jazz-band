
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
for bar in range(1):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(0, 8):
        hihat = pretty_midi.Note(velocity=90, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick2, snare1, snare2])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=63, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=90, pitch=65, start=2.25, end=2.625), # F
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=3.0),  # G
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=3.375, end=3.75), # Bb
    pretty_midi.Note(velocity=90, pitch=72, start=3.75, end=4.125), # B
    pretty_midi.Note(velocity=90, pitch=74, start=4.125, end=4.5),  # C
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=76, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=90, pitch=77, start=4.875, end=5.25), # Eb
    pretty_midi.Note(velocity=90, pitch=79, start=5.25, end=5.625), # F
    pretty_midi.Note(velocity=90, pitch=81, start=5.625, end=6.0),  # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
# Bar 2: D7 on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=74, start=1.875, end=2.25), # G
    pretty_midi.Note(velocity=100, pitch=77, start=1.875, end=2.25), # Bb
    pretty_midi.Note(velocity=100, pitch=79, start=1.875, end=2.25), # C
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25), # A
    # Bar 3: D7 on 2 and 4
    pretty_midi.Note(velocity=100, pitch=74, start=3.375, end=3.75), # G
    pretty_midi.Note(velocity=100, pitch=77, start=3.375, end=3.75), # Bb
    pretty_midi.Note(velocity=100, pitch=79, start=3.375, end=3.75), # C
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75), # A
    # Bar 4: D7 on 2 and 4
    pretty_midi.Note(velocity=100, pitch=74, start=4.875, end=5.25), # G
    pretty_midi.Note(velocity=100, pitch=77, start=4.875, end=5.25), # Bb
    pretty_midi.Note(velocity=100, pitch=79, start=4.875, end=5.25), # C
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25), # A
]
piano.notes.extend(piano_notes)

# Drums: same pattern continues for bars 2-4
for bar in range(2, 4):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(0, 8):
        hihat = pretty_midi.Note(velocity=90, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick2, snare1, snare2])

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D (62) -> F# (66) -> D (62) -> F# (66) -> D (62)
# Start it in bar 2, leave it hanging, come back in bar 4
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=110, pitch=66, start=1.75, end=2.0),   # F#
    # Bar 3
    pretty_midi.Note(velocity=110, pitch=62, start=2.0, end=2.25),  # D
    pretty_midi.Note(velocity=110, pitch=66, start=2.25, end=2.5),   # F#
    # Bar 4
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=110, pitch=66, start=4.75, end=5.0),   # F#
    pretty_midi.Note(velocity=110, pitch=62, start=5.0, end=5.25),  # D
    pretty_midi.Note(velocity=110, pitch=66, start=5.25, end=5.5),   # F#
    pretty_midi.Note(velocity=110, pitch=62, start=5.5, end=5.75),  # D
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_russo_intro.mid")
