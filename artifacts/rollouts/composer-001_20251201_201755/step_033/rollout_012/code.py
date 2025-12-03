
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
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass line: walking line with chromatic approaches
bass_notes = [
    # Bar 2: F (root) with chromatic approach
    pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=47, start=1.875, end=2.125),
    pretty_midi.Note(velocity=90, pitch=50, start=2.125, end=2.5),
    # Bar 3: Bb (fifth) with chromatic approach
    pretty_midi.Note(velocity=90, pitch=57, start=2.5, end=2.875),
    pretty_midi.Note(velocity=90, pitch=56, start=2.875, end=3.125),
    pretty_midi.Note(velocity=90, pitch=59, start=3.125, end=3.5),
    # Bar 4: C (major third) with chromatic approach
    pretty_midi.Note(velocity=90, pitch=52, start=3.5, end=3.875),
    pretty_midi.Note(velocity=90, pitch=51, start=3.875, end=4.125),
    pretty_midi.Note(velocity=90, pitch=54, start=4.125, end=4.5),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Fmaj7 (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=52, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=3.0),
    # Bar 3: Bbmaj7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=52, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=4.5),
    # Bar 4: C7 (C, E, G, Bb)
    pretty_midi.Note(velocity=100, pitch=52, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=55, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=6.0),
]
piano.notes.extend(piano_notes)

# Drums: Bar 2-4
# Kick on 1 and 3
for bar in [2, 3, 4]:
    kick_start = (bar - 1) * 1.5
    pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=kick_start + 1.125, end=kick_start + 1.5)
# Snare on 2 and 4
for bar in [2, 3, 4]:
    snare_start = (bar - 1) * 1.5 + 0.75
    pretty_midi.Note(velocity=110, pitch=38, start=snare_start, end=snare_start + 0.125)
    pretty_midi.Note(velocity=110, pitch=38, start=snare_start + 0.75, end=snare_start + 0.875)
# Hi-hat on every eighth
for bar in [2, 3, 4]:
    for i in range(8):
        hihat_start = (bar - 1) * 1.5 + i * 0.1875
        pretty_midi.Note(velocity=80, pitch=42, start=hihat_start, end=hihat_start + 0.1875)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Bar 2: Motif start
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),  # G
    pretty_midi.Note(velocity=110, pitch=65, start=1.75, end=2.0),  # Bb
    pretty_midi.Note(velocity=110, pitch=67, start=2.0, end=2.25),  # C
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.5),  # C
    # Bar 4: Come back and finish it
    pretty_midi.Note(velocity=110, pitch=65, start=4.5, end=4.75),  # Bb
    pretty_midi.Note(velocity=110, pitch=62, start=4.75, end=5.0),  # G
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.save('wayne_intro.mid')
