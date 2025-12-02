
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
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking bass line in F (D2-G2, MIDI 38-43)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875), # F (D2) root
    pretty_midi.Note(velocity=100, pitch=41, start=1.875, end=2.25), # Bb (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625), # C (fifth)
    pretty_midi.Note(velocity=100, pitch=40, start=2.625, end=3.0), # Ab (chromatic approach)
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, resolve on the last bar
piano_notes = []
# Bar 2: Fmaj7 (F A C E)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=1.875), # A
    pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=1.875), # C
    pretty_midi.Note(velocity=100, pitch=80, start=1.5, end=1.875), # E
])
# Bar 3: Bbmaj7 (Bb D F A)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625), # Bb
    pretty_midi.Note(velocity=100, pitch=70, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625), # F
    pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=2.625), # A
])
# Bar 4: C7 (C E G Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=77, start=2.625, end=3.0), # C
    pretty_midi.Note(velocity=100, pitch=80, start=2.625, end=3.0), # E
    pretty_midi.Note(velocity=100, pitch=81, start=2.625, end=3.0), # G
    pretty_midi.Note(velocity=100, pitch=74, start=2.625, end=3.0), # Bb
])
piano.notes.extend(piano_notes)

# Dante: Sax melody (motif, start and end)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875), # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25), # B
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625), # C
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0), # B
]
sax.notes.extend(sax_notes)

# Bar 2: Drums continue
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),
])
drums.notes.extend(drum_notes)

# Bars 3-4: Drums continue with kick on 1 and 3, snare on 2 and 4
for bar in range(2, 4):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 1.5)
    # Add to drums
    drums.notes.extend([kick1, kick2, snare1, snare2, hihat1])

midi.instruments.extend([sax, bass, piano, drums])
