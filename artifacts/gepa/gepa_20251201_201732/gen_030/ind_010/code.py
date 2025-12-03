
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
    hihat_1 = pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375)
    hihat_2 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat_3 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat_4 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick, snare, hihat_1, hihat_2, hihat_3, hihat_4])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: D2 (MIDI 38), chromatic approach to G2 (MIDI 43)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=100, pitch=39, start=1.875, end=2.25), # Eb2 (chromatic)
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625),  # G2
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),  # F2 (chromatic)
    pretty_midi.Note(velocity=100, pitch=43, start=3.0, end=3.375),  # G2
    pretty_midi.Note(velocity=100, pitch=44, start=3.375, end=3.75), # Ab2 (chromatic)
    pretty_midi.Note(velocity=100, pitch=43, start=3.75, end=4.125), # G2
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),  # F2 (chromatic)
    pretty_midi.Note(velocity=100, pitch=43, start=4.5, end=4.875),  # G2
    pretty_midi.Note(velocity=100, pitch=44, start=4.875, end=5.25), # Ab2 (chromatic)
    pretty_midi.Note(velocity=100, pitch=43, start=5.25, end=5.625), # G2
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),  # F2 (chromatic)
]
bass.notes.extend(bass_notes)

# Piano: open voicings, different chord each bar
# Bar 2: D7 (D-F#-A-C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.25),  # D4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.25),  # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.25),  # A4
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=2.25),  # C4
]
piano.notes.extend(piano_notes)

# Bar 3: G7 (G-B-D-F)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=3.0),  # G4
    pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=3.0),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=3.0),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=3.0),  # F4
]
piano.notes.extend(piano_notes)

# Bar 4: A7 (A-C#-E-G)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.75),  # A4
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.75),  # C#5
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.75),  # E5
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.75),  # G4
]
piano.notes.extend(piano_notes)

# Saxophone: one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Start on D4, then move to Bb4, then end on D4 again
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=70, start=1.875, end=2.25),  # Bb4
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),   # D4
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),  # D4
    pretty_midi.Note(velocity=100, pitch=70, start=3.75, end=4.125),  # Bb4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),   # D4
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625),  # D4
    pretty_midi.Note(velocity=100, pitch=70, start=5.625, end=6.0),   # Bb4
]
sax.notes.extend(sax_notes)

# Drums: continue with kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    start = bar * 1.5
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    hihat_1 = pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375)
    hihat_2 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat_3 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat_4 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick, snare, hihat_1, hihat_2, hihat_3, hihat_4])

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
