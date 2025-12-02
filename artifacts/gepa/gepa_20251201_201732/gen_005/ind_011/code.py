
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_kick = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
drum_snare = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)
drum_hihat = pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5)
drum_hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75)
drum_hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125)
drum_hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5)
drums.notes.extend([drum_kick, drum_snare, drum_hihat, drum_hihat2, drum_hihat3, drum_hihat4])

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line, D2-G2, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25), # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625), # G2
    pretty_midi.Note(velocity=100, pitch=45, start=2.625, end=3.0),  # A2 (fifth of D)
]
bass.notes.extend(bass_notes)

# Piano: open voicings, resolve on the last
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=55, start=1.5, end=1.875),  # C7
    pretty_midi.Note(velocity=100, pitch=59, start=1.5, end=1.875),  # E7
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # G7
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25), # B7
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625), # D8
    pretty_midi.Note(velocity=100, pitch=74, start=2.625, end=3.0),  # F8
]
piano.notes.extend(piano_notes)

# Sax: one short motif, make it sing. Start it, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # G4
    pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=2.0),   # Bb4
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),  # C5
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),  # G4
    pretty_midi.Note(velocity=100, pitch=65, start=2.5, end=2.75),  # Bb4
    pretty_midi.Note(velocity=100, pitch=67, start=2.75, end=3.0),  # C5
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: walking line, D2-G2, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=45, start=3.0, end=3.375),  # A2
    pretty_midi.Note(velocity=100, pitch=43, start=3.375, end=3.75),  # G2
    pretty_midi.Note(velocity=100, pitch=40, start=3.75, end=4.125),  # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),   # D2
]
bass.notes.extend(bass_notes)

# Piano: open voicings, resolve on the last
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=59, start=3.0, end=3.375),  # E7
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),  # A7
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # C8
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75), # D8
    pretty_midi.Note(velocity=100, pitch=74, start=3.75, end=4.125), # F8
    pretty_midi.Note(velocity=100, pitch=76, start=4.125, end=4.5),  # G8
]
piano.notes.extend(piano_notes)

# Sax: continue motif, return to the beginning
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # G4
    pretty_midi.Note(velocity=100, pitch=65, start=3.25, end=3.5),   # Bb4
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75),  # C5
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0),  # G4
    pretty_midi.Note(velocity=100, pitch=65, start=4.0, end=4.25),  # Bb4
    pretty_midi.Note(velocity=100, pitch=67, start=4.25, end=4.5),  # C5
]
sax.notes.extend(sax_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i in range(3):
    kick_start = 1.5 + i * 1.5
    kick = pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_start + 0.375)
    snare_start = kick_start + 0.75
    snare = pretty_midi.Note(velocity=100, pitch=38, start=snare_start, end=snare_start + 0.375)
    hihat_start = kick_start
    hihat = pretty_midi.Note(velocity=100, pitch=42, start=hihat_start, end=hihat_start + 0.375)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=hihat_start + 0.375, end=hihat_start + 0.75)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=hihat_start + 0.75, end=hihat_start + 1.125)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=hihat_start + 1.125, end=hihat_start + 1.5)
    drums.notes.extend([kick, snare, hihat, hihat2, hihat3, hihat4])

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: walking line, D2-G2, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # D2
    pretty_midi.Note(velocity=100, pitch=40, start=4.875, end=5.25),  # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=43, start=5.25, end=5.625),  # G2
    pretty_midi.Note(velocity=100, pitch=45, start=5.625, end=6.0),   # A2 (fifth of D)
]
bass.notes.extend(bass_notes)

# Piano: open voicings, resolve on the last
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=55, start=4.5, end=4.875),  # C7
    pretty_midi.Note(velocity=100, pitch=59, start=4.5, end=4.875),  # E7
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # G7
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25), # B7
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.625), # D8
    pretty_midi.Note(velocity=100, pitch=74, start=5.625, end=6.0),  # F8
]
piano.notes.extend(piano_notes)

# Sax: finish the motif, return to the beginning
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # G4
    pretty_midi.Note(velocity=100, pitch=65, start=4.75, end=5.0),   # Bb4
    pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.25),  # C5
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5),  # G4
    pretty_midi.Note(velocity=100, pitch=65, start=5.5, end=5.75),  # Bb4
    pretty_midi.Note(velocity=100, pitch=67, start=5.75, end=6.0),  # C5
]
sax.notes.extend(sax_notes)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Write MIDI file
midi.write("dante_intro.mid")
