
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

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = []
for bar in range(1):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125))
        if beat == 1 or beat == 3:
            drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125))
        for eighth in range(2):
            drum_notes.append(pretty_midi.Note(velocity=60, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625))

drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: walking line, roots and fifths with chromatic approaches, D2-G2, MIDI 38-43
bass_notes = []
for bar in range(2, 5):
    time = (bar - 2) * 1.5
    if bar == 2:
        # D2 (38) -> Eb2 (39) -> G2 (43) -> A2 (45)
        bass_notes.append(pretty_midi.Note(velocity=80, pitch=38, start=time, end=time + 0.25))
        bass_notes.append(pretty_midi.Note(velocity=80, pitch=39, start=time + 0.25, end=time + 0.5))
        bass_notes.append(pretty_midi.Note(velocity=80, pitch=43, start=time + 0.5, end=time + 0.75))
        bass_notes.append(pretty_midi.Note(velocity=80, pitch=45, start=time + 0.75, end=time + 1.0))
    elif bar == 3:
        # G2 (43) -> Ab2 (44) -> B2 (46) -> C3 (48)
        bass_notes.append(pretty_midi.Note(velocity=80, pitch=43, start=time, end=time + 0.25))
        bass_notes.append(pretty_midi.Note(velocity=80, pitch=44, start=time + 0.25, end=time + 0.5))
        bass_notes.append(pretty_midi.Note(velocity=80, pitch=46, start=time + 0.5, end=time + 0.75))
        bass_notes.append(pretty_midi.Note(velocity=80, pitch=48, start=time + 0.75, end=time + 1.0))
    elif bar == 4:
        # B2 (46) -> C3 (48) -> D3 (50) -> Eb3 (51)
        bass_notes.append(pretty_midi.Note(velocity=80, pitch=46, start=time, end=time + 0.25))
        bass_notes.append(pretty_midi.Note(velocity=80, pitch=48, start=time + 0.25, end=time + 0.5))
        bass_notes.append(pretty_midi.Note(velocity=80, pitch=50, start=time + 0.5, end=time + 0.75))
        bass_notes.append(pretty_midi.Note(velocity=80, pitch=51, start=time + 0.75, end=time + 1.0))

bass.notes.extend(bass_notes)

# Diane on piano: open voicings, different chord each bar, resolve on the last
piano_notes = []
for bar in range(2, 5):
    time = (bar - 2) * 1.5
    if bar == 2:
        # Dmaj7: D, F#, A, C#
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=62, start=time, end=time + 0.5))
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=67, start=time, end=time + 0.5))
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=71, start=time, end=time + 0.5))
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=73, start=time, end=time + 0.5))
    elif bar == 3:
        # G7: G, B, D, F
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=67, start=time, end=time + 0.5))
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=71, start=time, end=time + 0.5))
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=74, start=time, end=time + 0.5))
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=76, start=time, end=time + 0.5))
    elif bar == 4:
        # Bm7: B, D, F#, A
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=71, start=time, end=time + 0.5))
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=74, start=time, end=time + 0.5))
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=77, start=time, end=time + 0.5))
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=79, start=time, end=time + 0.5))

piano.notes.extend(piano_notes)

# Dante on sax: one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = []
time = 1.5  # start of bar 2
# Motif: D (62), F# (67), B (71), D (62)
sax_notes.append(pretty_midi.Note(velocity=110, pitch=62, start=time, end=time + 0.375))
sax_notes.append(pretty_midi.Note(velocity=110, pitch=67, start=time + 0.375, end=time + 0.75))
sax_notes.append(pretty_midi.Note(velocity=110, pitch=71, start=time + 0.75, end=time + 1.125))
sax_notes.append(pretty_midi.Note(velocity=110, pitch=62, start=time + 1.5, end=time + 1.875))

sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
